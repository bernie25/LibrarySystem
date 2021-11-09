from django.shortcuts import render,HttpResponse,redirect
#Render: HttpResponse object is returned and it also combines the template with the dictionary that is passed in render.
# HttpResponse:Text Response is displayed to the user with HttpResponse.
#Redirect: It redirects the user to the desired page.
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
#Authorization and authentication are handled with User.
from django.contrib import messages
#It helps in displaying messages to the user.
from datetime import datetime,timedelta,date
from .models import IssueBook, UserExtend,AddBook,returnBook,AddStudent
#A person can only log in if the user is a registered user.
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as dj_login
from views.userfactory import Userfactory


#index() redirects to the home page.
def index(request):
    return render(request,'index.html')

#staff() redirects to the staff page where a person gets the option to sign up and login.
def staff(request):
    return render(request,'staff.html')

#staffLogin() redirects to the login page if a person is not logged in and if a person is logged in he/she will be redirected to the dashboard.
def staffLogin(request):
    if request.session.has_key('is_logged'):
        return redirect('dashboard')
    return render(request,'staffLogin.html')

#staffSignup() redirects to the signup page.
def staffSignup(request):
    return render(request,'staffSignup.html')

#Dashboard & displays all the books that are added.
def dashboard(request):
    if request.session.has_key('is_logged'):
        Book = AddBook.objects.all()
        return render(request,'dashboard.html',{'Book':Book})
    return redirect('staffLogin')

#addbook() redirects to the page where the book can be added.
def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'addBook.html',{'Book':Book})

# signupBackend() handles the backend of signup form.
def signupBackend(request):
    if request.method =='POST':
            uname = request.POST["uname"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email = request.POST["email"]
            phone=request.POST['phone']
            password=request.POST['password']
            userprofile = UserExtend(phone=phone)
            if request.method == 'POST':
                try:
                    UserExists = User.objects.get(username=request.POST['uname'])
                    messages.error(request," Username already taken, Try something else!!!")
                    return redirect("staffSignup")    
                except User.DoesNotExist:
                    if len(uname)>10:
                        messages.error(request," Username must be max 15 characters, Please try again")
                        return redirect("staffSignup")
            
                    if not uname.isalnum():
                        messages.error(request," Username should only contain letters and numbers, Please try again")
                        return redirect("staffSignup")
            
            # create the user
            user = User.objects.create_user(uname, email, password)
            user.first_name=fname
            user.last_name=lname
            user.email = email
            user.save()
            userprofile.user = user
            userprofile.save()
            messages.success(request," Your account has been successfully created")
            return redirect("staffLogin")
    else:
        return HttpResponse('404 - NOT FOUND ')

#loginBackend() handles the backend of login form. To sign up a person needs to enter the username,
#  first name , last name , email , phone number and password.
#loginBackend() checks whether a person is a registered user or not. 
# If the person is registered he/she will be directed to the dashboard.
def loginBackend(request):
    if request.method =='POST':
        loginuname = request.POST["loginuname"]
        loginpassword=request.POST["loginpassword"]
        RegisteredUser = authenticate(username=loginuname, password=loginpassword)
        if RegisteredUser is not None:
            dj_login(request, RegisteredUser)
            request.session['is_logged'] = True
            RegisteredUser = request.user.id 
            request.session["user_id"] = RegisteredUser
            messages.success(request, " Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request," Invalid Credentials, Please try again")  
            return redirect("/")  
    return HttpResponse('404-not found')

#register user Factory 
def register(request):
    if request.method == 'POST':
        factory = Userfactory()
        form = signupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            factory.createuser(form, newuser)
            newuser.is_active = False
            newuser.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your library account'
            message = render_to_string('registration/acc_active_email.html', {
                'user': newuser,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)).decode(),
                'token': account_activation_token.make_token(newuser),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})


#Avrivation 
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')








#adding a book submossion
def AddBookSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            bookid = request.POST["bookid"]
            bookname = request.POST["bookname"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            add = AddBook(user = user1,bookid=bookid,bookname=bookname,subject=subject,category=category)
            add.save()
            Book = AddBook.objects.all()
            return render(request,'dashboard.html',{'Book':Book})
    return redirect('/')

#eletebook() deletes the details of the book that is added. If a user is logged in, the selected row will be deleted with the help of delete() and after deleting the user will be redirected to the dashboard.
def deleteBook(request,id):
    if request.session.has_key('is_logged'):
        AddBook_info = AddBook.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("login") 

#bookIssue() redirects the user to the page where the book can be issued by entering the details of bookid and studentid.
def bookIssue(request):
    return render(request,'bookIssue.html')

#redirects the user to the page where the book can be returned by entering the bookid.
def returnBook(request):
    return render(request,'returnBook.html')

#Logging out
def HandleLogout(request):
        del request.session['is_logged']
        del request.session["user_id"] 
        logout(request)
        messages.success(request, " Successfully logged out")
        return redirect('dashboard')

#issuebooksubmission() handles the backend of the form. It takes the information of bookid and studentid and stores it in the database and also it changes the status of the book from Not-Issued to Issued in the database as well as in the table that is displayed on the dashboard.
def issueBookSubmission(request):
       if request.method=='POST':
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            studentid=request.POST['studentid']
            book1=request.POST['book1']
            store=AddBook.objects.filter(bookid=book1)
            def get_category(addbook):
                if addbook.category=="Not-Issued":
                    addbook.category="Issued"
                    obj= IssueBook(user=user1,studentid=studentid,book1=book1)
                    obj.save()
                    addbook.save()
                else:
                    messages.error(request," Book already issued !!!")
            category_list=list(set(map(get_category,store)))         
            Issue=IssueBook.objects.all()
            return render(request,'bookIssue.html',{'Issue':Issue})
       return redirect('/')

#vhandles the backend of the return book page. 
#stores the bookid of the book that is returned in the database and also it changes the status of the book to Not-Issued in the database as well as in the table displayed on the dashboard.
def returnBooksubmission(request):
    if request.method=='POST':
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            bookid2=request.POST['bookid2']
            store1=AddBook.objects.filter(bookid=bookid2)
            def return_book(returnBook):
                if returnBook.category=="Issued":
                    returnBook.category="Not-Issued"
                    obj1=returnBook(user=user1,bookid2=bookid2)
                    obj=IssueBook.objects.filter(book1=bookid2)
                    obj.delete()
                    obj1.save()
                    returnBook.save()
                else:
                    messages.error(request," Book not  issued !!!")
            returncategorylist=list(set(map(return_book,store1)))
            Return= returnBook.objects.all()
            return render(request,'returnBook.html',{'Return':Return})
    return redirect('/')


#Search() helps in searching the information related to books displayed on the dashboard.
#he user can get the details of the book by entering the bookid in the search bar.
def Search(request):
    if request.session.has_key('is_logged'):
        query2=request.GET["query2"]
        Book=AddBook.objects.filter(bookid__icontains=query2)
        params={'Book':Book}
        return render(request,'dashboard.html',params)
    return redirect("login") 

#gets the details of the book which is to be edited and opens the edit form.
def editbookDetails(request,id):
    if request.session.has_key('is_logged'):
        Book = AddBook.objects.get(id=id)
        return render(request,'editDetails.html',{'Book':Book})
    return redirect('login')

#stores the new details of the user in the database and updates the details in the table displayed on the dashboard.
def updateDetails(request,id):
    if request.session.has_key('is_logged'):
        if request.method=="POST":
                add=AddBook.objects.get(id=id)
                add.bookid=request.POST["bookid"]
                add.bookname=request.POST["bookname"]
                add.subject=request.POST["subject"]
                add.ContactNumber=request.POST['category']
                add.save()
                return redirect("dashboard")
    return redirect('login')

#add student
def AddSudent(request):
    if request.session.has_key('is_logged'):
       return render(request,'addStudent.html')
    return redirect ('login')

#view student list
def viewstudents(request):
    if request.session.has_key('is_logged'):
        Student=AddStudent.objects.all()
        return render(request,'viewStudents.html',{'Student':Student})
    return redirect('staffLogin')

#search the students that are registered.
def Searchstudent(request):
    if request.session.has_key('is_logged'):
        query3=request.GET["query3"]
        Student=AddStudent.objects.filter(studentid__icontains=query3)
        params={'Student':Student}
        return render(request,'viewstudents.html',params)
    return redirect("staffLogin") 
#handles the backend of the addstudent form
def addstudentsubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            sname = request.POST["sname"]
            studentid = request.POST["studentid"]
            add = AddStudent(user = user1,sname=sname,studentid=studentid)
            add.save()
            Student = AddStudent.objects.all()
            return render(request,'addStudent.html',{'Student':Student})
    return redirect('/')

#view all issued books.
def viewissuedbook(request):
    if request.session.has_key('is_logged'):
        issuedbooks=IssueBook.objects.all()
        lis=[]
        li=[]
        
        for books in issuedbooks:
            issdate=str(books.issuedate.day)+'-'+str(books.issuedate.month)+'-'+str(books.issuedate.year)
            expdate=str(books.expirydate.day)+'-'+str(books.expirydate.month)+'-'+str(books.expirydate.year)
            #fine calculation
            days=(date.today()-books.issuedate)
            d=days.days
            fine=0
            if d>15:
                day=d-15
                fine=day*10
            print(d)

            book=list(AddBook.objects.filter(bookid=books.book1))
            students=list(AddStudent.objects.filter(studentid=books.studentid))
            print(book)
            print(students)
            i=0
            for k in book:
                print(li)
                t=(students[i].sname,students[i].studentid,book[i].bookname,book[i].subject,issdate,expdate,fine)
                print(t)
                i=i+1
                lis.append(t)
                print(lis)

        return render(request,'viewIssuedBook.html',{'lis':lis})
    return redirect('/')

    #Still implement design patterns & implement different fines for different books and maybe admin?
    

