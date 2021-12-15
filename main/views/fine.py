##penalty
#from views.views import Student

# def Fine(request):
#     student = Student.objects.filter(user_id=request.user.id)
#     #issuedBooks = book.objects.filter(student.user_id)
#     #issuedBooks = IssuedBook.objects.filter(student_number=student[0].user_id)
#     li1 = []
#     li2 = []
#     for i in issuedBooks:
#         books = Book.objects.filter(bookcode=i.bookcode)
#         for book in books:
#             t=(request.user.id, request.user.get_full_name, book.name)
#             li1.append(t)

#         days=(date.today()-i.issued_date)
#         d=days.days
#         fine=0
#         if d>15:
#             day=d-14
#             fine=day*5
#         t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
#         li2.append(t)
#     return render(request,'...html',{'li1':li1, 'li2':li2})
