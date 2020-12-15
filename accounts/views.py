from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


def accounts(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method == 'POST':
        # The user wants to sign up!
        if request.POST['password'] == request.POST['password_confirmation']:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
    else:
        # The User wants to enter info
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # todo need to logout to home page and logout
    return render(request, 'accounts/signup.html')
