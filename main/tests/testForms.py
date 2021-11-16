from forms.forms import SignUpForm
from django.test import TestCase


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        self.assertTrue(form.fields['first_name'].label is None)
        self.assertTrue(form.fields['last_name'].label is None)
        self.assertTrue(form.fields['phone'].label is None)
        self.assertTrue(form.fields['email'].label is None)

    #Test sign up success

    #Test sign up failure
