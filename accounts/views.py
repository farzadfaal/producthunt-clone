from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def accounts(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method == 'POST':
        # The user wants to sign up!
        if request.POST['password'] == request.POST['password_confirmation']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords Doesn\'t match'})
    else:
        # The User wants to enter info
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and/or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # todo need to logout to home page and logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')
