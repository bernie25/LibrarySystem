from main.models import Student
from main.models import Librarian

class UserFactory():
    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        idnumber= form.cleaned_data.get('id no')
        if "@outlook.at" in email:
            newuser = Librarian.objects.create_staff(user)
        else:
            newuser = Student.objects.create_student(user, idnumber)

        newuser.save()
