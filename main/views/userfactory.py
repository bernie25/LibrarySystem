from main.models import Student
from main.models import Librarian

class UserFactory():
    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        id_no = form.cleaned_data.get('id no')
        if "@outlook.at" in email:
            newuser = Librarian.objects.create_staff(user)
        else:
            newuser = Student.objects.create_student(user, id_no)

        newuser.save()
