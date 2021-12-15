from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name')
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address.')
    idnumber = forms.CharField(max_length=255, help_text='Please Enter ID number')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'idnumber', 'email', 'password1', 'password2',)


