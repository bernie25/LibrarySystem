
from models.user.patron import Patron
from models.user.librarian import Librarian


class Userfactory():
    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        id_no = form.cleaned_data.get('id no')
        phone = form.cleaned_data.get('phone')
        if "@outlook.at" in email:
            newuser = Librarian.objects.create_staff(user)
        else:
            newuser = Patron.objects.create_student(user, id_no, phone)

        newuser.save()
