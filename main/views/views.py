from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Student, User
from main.services.requestBook.bookreq import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.views.book import Book
from datetime import date
from main.forms import bookform

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render
from main.models import *
from django.shortcuts import render
from main.forms.signupform import SignUpForm
from main.views.userfactory import UserFactory
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required

# from .forms import RenewBookForm
from main.forms.renewbookform import RenewBookForm

from django.urls import reverse_lazy
from main.models import Author
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


def homePage(request):
    return render(request, 'homePage.html')

def index(request):
    return HttpResponse("Hello")

#Add a book to the library
def addBook(request):
    if request.method == 'POST':
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
    context = {
        'title' : "Add Book",
    }
    return render(request, 'addBook.html', context=context)

#Booking
def booking(request):
    return render(request, 'booking.html')

@login_required(login_url='login')
def home(request):
		if(request.GET.get('mybtn')):
			print("Book now available") 
		return render(request, '../templates/requestBook.html')
		# bookAvailableClass()

def reqbook(request):
		return render(request,'../templates/requestBook.html')

def signup(request):
		return render(request,'../templates/signup.html')
        
def logout(request):
		return render(request,'../templates/logout.html')

#Create Library
def libraryView(request, *args, **kwargs):
    
    view_all_library = Book.objects.all()
    return render(request, '../templates/library.html', 
    {'view_all_library': view_all_library})

def issue_book(request):
    form = bookform()
    if request.method == "POST":
        form = bookform(request.POST)
        if form.is_valid():
            obj = models.issued_book()
            obj.student_number = form.cleaned_data['student_number']
            obj.bookcode = request.POST['bookcode2']
            obj.save()
            alert = True
            return render(request, "issued_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issued_book.html", {'form':form})


def IssuedBook(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(student.user_id)
    #issuedBooks = IssuedBook.objects.filter(student_number=student[0].user_id)
    li1 = []
    li2 = []
    for i in issuedBooks:
        books = Book.objects.filter(bookcode=i.bookcode)
        for book in books:
            t=(request.user.id, request.user.get_full_name, book.name)
            li1.append(t)

        days=(date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>15:
            day=d-14
            fine=day*5
        t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
        li2.append(t)
    return render(request,'studentIssuedBook.html',{'li1':li1, 'li2':li2})

#Signup basic registration function
def signup(request):
    if request.method == 'POST':
        factory = UserFactory()
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            factory.createuser(form, new_user)
            new_user.save()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if (user is not None and default_token_generator.check_token(user, token)):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, 'Account activated. Please login.')
    else:
        messages.add_message(request, messages.INFO, 'Link Expired. Contact admin to activate your account.')

    return redirect('login.html')

######################################
from main.models import Book, Author, BookInstance, Category

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

######################################
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,  generic.ListView):
    """ view listing books on loan to current user."""
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'can_mark_returned'
    template_name = 'bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('can_mark_returned', raise_exception=True)
#book delete
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)
 # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
            'form': form,
            'book_instance': book_instance,
        }

    return render(request, 'book_renew_librarian.html', context)

class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['bookname', 'author', 'bookcode' 'category']

class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')


    
