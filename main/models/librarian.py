from django.db import models
from models import User

class Librarianmanager(models.Manager):
    def create_librarian(self, user):
        id=user.id
        newuser=self.model(user_id=id)
        newuser.save(using=self._db)
        return newuser

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    objects=Librarianmanager()
