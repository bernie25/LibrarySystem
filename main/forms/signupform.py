from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    id_no = forms.CharField(max_length=19, help_text='Please enter your ID number')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'id_no', 'password1', 'password2',)
