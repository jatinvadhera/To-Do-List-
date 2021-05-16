from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['name']
        #last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(first_name=first_name).exists():
                messages.info(request, 'Username taken')
                return redirect('/')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('/')
            else:
                user = User.objects.create_user(
                    password=password1, email=email, first_name=first_name, username=username)
                user.save()
                messages.info(request, 'User Created')
                return redirect('/login')
        else:
            messages.info(
                request, 'Password and confirm password are not matching')
            return redirect('form-register.html')
    else:
        return render(request, 'form-register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/todo')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'form-login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfully Logged out')
    return redirect('/')


def thanks(request):
    return render(request, 'thanks.html')
