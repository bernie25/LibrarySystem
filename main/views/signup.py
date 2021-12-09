from django.shortcuts import render, redirect
from main.forms.signupform import SignUpForm
from main.models import Student
from main.views.userfactory import UserFactory
from django.contrib.auth import authenticate, login


#Signup basic registration function
def signup(request):
    if request.method == 'POST':
        factory = UserFactory()
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            factory.createuser(form, user)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})