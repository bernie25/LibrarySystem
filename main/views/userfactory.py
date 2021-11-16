from models.user.student import Student
from models.user.staff import Staff


class Userfactory():

    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        id_no = form.cleaned_data.get('id no')
        phone = form.cleaned_data.get('phone')
        if "@outlook.at" in email:
            newuser = Staff.objects.create_librarian(email=emailuser)
        else:
            newuser = Student.objects.create_student(user, id_no, phone)

        newuser.save()
