from django.db import models
from main.models.user import User

class Studentmanager(models.Manager):
    def create_student(self, user, id_no, telephone):
        id=user.id
        newuser=self.model(user_id=id, phone=telephone, id_no=id_no)
        newuser.save(using=self._db)
        return newuser

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=17, blank=True)
    credit_card = models.CharField(max_length=19)
    objects=Studentmanager()
