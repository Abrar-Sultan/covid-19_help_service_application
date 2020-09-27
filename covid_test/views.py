from django.shortcuts import render
from covid_test import models

def test_online(request):
    """
    This method is used to display home page of request for covid test service online.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a home page of request for covid test service online which is a HTML page if
    the user is logged in. else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return render(request,"Test_Online.html")

def thank_you(request):
    """
    This method is used to handle request from of covid test, it takes data from the form
    and stores it in the database that is for online test request.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base if the user is logged in. else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":
            contact_number = request.POST['Contact_Number']
            f_name = request.POST['F_Name']
            nidbc = request.POST['NIDBC']
            l_name = request.POST['L_name']
            age = request.POST['Age']
            address = request.POST['Address']
            ins = models.OnlineTest(first_name=f_name, last_name=l_name, nid_or_birth_certificate=nidbc, age=age, address=address, contact_number=contact_number)
            ins.save()
        return render(request,"Thank_You.html")