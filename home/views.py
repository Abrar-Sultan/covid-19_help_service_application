from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    """
    This method is used to display home page.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a home page
     which is a HTML page.


    :rtype: HttpResponse.
    """
    return render(request, 'index.html')


def register(request):
    """
    This method is used to register nre users.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a  login page after successfull
    registration.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return render(request, 'register.html')

            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=f_name,
                                                last_name=l_name)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password is not Matching')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')


def login(request):
    """
    This method is used to login a user.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a home page
     which is a HTML page.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid Credentials')
            # return render('')

    else:
        return render(request, 'login.html')


def logout(request):
    """
    This method is used to logout user.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a home page
     which is a HTML page.


    :rtype: HttpResponse.
    """
    auth.logout(request)
    return render(request, 'index.html')

