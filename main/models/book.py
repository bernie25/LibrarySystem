from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=30, blank=True)
    bookcode = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)

    def __str__(self) -> str: return self.bookname and self.category and self.bookcode
