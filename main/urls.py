from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('staff/',views.staff,name='staff'),
    path('staffLogin/',views.staffLogin,name='staffLogin'),
    path('staffSignup/',views.staffSignup,name='staffSignup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addBook/',views.addBook,name='addBook'),
    path('SignupBackend/',views.signupBackend,name='SignupBackend'),
    path('loginBackend/',views.loginBackend,name='loginBackend'),
    path('AddBookSubmission/',views.addBookSubmission,name='AddBookSubmission'),
    path('deleteBook/<int:id>',views.deleteBook,name='deleteBook'),
    path('bookIssue/',views.bookIssue,name='bookIssue'),
    path('returnBook/',views.returnBook,name='returnBook'),
    path('HandleLogout/',views.HandleLogout,name='HandleLogout'),
    path('issueBookSubmission/',views.issueBookSubmission,name='issueBookSubmission'),
    path('returnBookSubmission/',views.returnBookSubmission,name='returnBookSubmission'),
    path('Search/',views.Search,name='Search'),
    path('searchStudent/',views.searchStudent,name='searchStudent'),
    path('editBookDetails/<int:id>',views.editBookDetails,name='editBookDetails'),
    path('<int:id>/updateDetails/',views.updateDetails,name='updateDetails'),
    path('addStudent/',views.addStudent,name='addStudent'),
    path('addStudentSubmission/',views.addStudentSubmission,name='addStudentSubmission'),
    path('viewIssuedBook/',views.viewIssuedBook,name='viewIssuedBook'),
    path('viewStudents/',views.viewStudents,name='viewStudents')
]
