#User Creation came from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


#UserCreationForm handling -
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #after this the user is created. 
            
            #manually authenticate the user. You could redirect the user to the login page, 
            #but performing the authentication is good for the user experience.
            username = form.cleaned_data.get('username')
            #to perform the authentication, we need to grab the raw password from the input that came from POST. The user.password stores the hash, 
            #and we can’t use it directly to authenticate.
            raw_password = form.cleaned_data.get('password1')
            #If the authenticate() function is executed successfully 
            # (in this case it will always return a success), 
            # it will a user instance (meaning the username and password matches),
            #  we can now securely log the user in. It’s done by calling the login() function, 
            # passing the request and the user instance as parameter.
            #  After that, simply redirect the user to wherever you want.
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index') #redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})