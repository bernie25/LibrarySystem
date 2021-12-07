from django.shortcuts import render
from main.forms.signupform import SignUpForm
from main.views.userfactory import UserFactory

#Signup basic registration function
def signup(request):
    factory = UserFactory()
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        factory.createuser(form, user)
        user.save()
    else:
            form = SignUpForm()
    return render(request, 'signup.html', {'form': form})