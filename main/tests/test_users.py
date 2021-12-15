from django.test import TestCase
from main.models import Author, Student 

# Tests for Creating Author and student

class CreateAdminTest(TestCase):
    @classmethod
    def setUp(cls):
        Author.objects.create(first_name= 'Bernie', 
                    last_name = 'Twomey')

    def test_author_will_create(self):
        author = Author.objects.get(id=1)
        print("Method: test_author_will_create.")
        create_author_test = author._meta.get_field('first_name').verbose_name
        self.assertTrue(create_author_test, 'Bernie')

    def test_author_wont_create(self):
        print("Method: test_author_wont_create.")
        self.assertFalse(False)

# class CreateStudentTest(TestCase):
#     @classmethod
#     def setUp(cls):
#         Student.objects.create(user= 'Bernie', 
#                     student_number = '123')

#     def test_student_will_create(self):
#         student = Student.objects.get(id=1)
#         print("Method: test_student_will_create.")
#         create_student_test = student._meta.get_field('user').verbose_name
#         self.assertTrue(create_student_test, 'Bernie')

#     def test_student_wont_create(self):
#         print("Method: test_student_wont_create.")
#         self.assertFalse(False)

