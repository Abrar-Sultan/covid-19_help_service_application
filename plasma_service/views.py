from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PlasmaRequest, PlasmaDonate
from django.contrib import messages


def plasma_home(request):
    """
    This method is used to display home page for this plasma service function.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a home page for plasma service
     which is a HTML page.


    :rtype: HttpResponse.
    """

    return render(request, 'plasma_home.html')


def request_plasma_form(request):
    """
    This method is used to display plasma request form only when the
    user is logged in, else it will display the login page for user to log in.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns login page when user
    is not logged in, else it returns the plasma request form.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        # messages.info(request, 'Please Login')
        return render(request, 'login.html')
    else:
        return render(request, 'request_plasma_form.html')


def request_plasma(request):
    """
    This method is used to handle plasma request form, it takes data from the form
    and stores it in the database that is for plasma request.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base, else it will return the plasma request
    form again.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        age = request.POST['age']
        sex = request.POST['sex']
        blood_group = request.POST['blood_group']
        nid = request.POST['nid']
        location = request.POST['location']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        img = request.FILES['image']

        if PlasmaRequest.objects.filter(nid=nid).exists():
            messages.info(request, 'Request Already Exists')
            return render(request, 'request_plasma_form.html')

        else:
            info = PlasmaRequest(username=request.user.username, first_name=f_name, last_name=l_name, age=age, sex=sex,
                                 email=email, nid=nid,
                                 blood_type=blood_group,
                                 phone_number=contact_number, location=location, image=img)

            info.save()
            return render(request, 'thank_you.html')
    else:
        return render(request, 'request_plasma_form.html')


def show_plasma_request(request):
    """
     This method is used to display the available plasma request list.


     :param request: it's a HttpResponse from user.


     :type request HttpResponse.


     :return: this method returns a html page that display all the available entry
     of the plasma request in the data base.


     :rtype: HttpResponse.
     """
    request_list = PlasmaRequest.objects.all()
    return render(request, 'show_plasma_request_list.html', {'request_list': request_list})


def search_request(request):
    """
      This method is used to search plasma request by blood group, it search all
      the records in the data base for a specific blood group and display the
      results.


      :param request: it's a HttpResponse from user.


      :type request HttpResponse.


      :return: this method returns a html page that display all the available entry
      of the plasma request in the data base that matches the users entry.


      :rtype: HttpResponse.
      """
    query = request.GET['query']
    if len(query) > 10:
        results = 'X'

    else:
        results = PlasmaRequest.objects.filter(blood_type__icontains=query)

    return render(request, 'search_plasma.html', {'results': results, 'query': query})


def delete_request_form(request):
    """
      This method is used to display the available plasma request list for a specific
      user and it displays a form for that user where user can input a id from the list
      to delete that particular request for plasma.


      :param request: it's a HttpResponse from user.


      :type request HttpResponse.


      :return: this method returns a html page. It returns login page when user
       is not logged in, else it returns the page that display form to delete and
       that users requests.


      :rtype: HttpResponse.
      """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        query = request.user.username
        user_entry = PlasmaRequest.objects.filter(username=query)
        return render(request, 'delete_request_form.html', {'user_entry': user_entry})


def delete_request(request):
    """
        This method is used to handle the delete functionality for plasma request
        for a specific user. It finds that particular entry of that user and delete
        that entry.


        :param request: it's a HttpResponse from user.


        :type request HttpResponse.


        :return: this method returns the home page for plasma service.


        :rtype: HttpResponse.
        """
    entry = request.POST['query']
    if PlasmaRequest.objects.filter(username=request.user.username, id=entry).exists():
        delete_entry = PlasmaRequest.objects.filter(username=request.user.username, id=entry)
        delete_entry.delete()
        return render(request, 'plasma_home.html')
    else:
        messages.info(request, 'Entry Does Not Exists')
        return render(request, 'delete_request_form.html')


def donate_plasma_form(request):
    """
     This method is used to display plasma donate request form only when the
     user is logged in, else it will display the login page for user to log in.


     :param request: it's a HttpResponse from user.


     :type request HttpResponse.


     :return: this method returns a html page. It returns login page when user
     is not logged in, else it returns the registration form for plasma donation.


     :rtype: HttpResponse.
     """
    if not request.user.is_authenticated:
        # messages.info(request, 'Please Login')
        return render(request, 'login.html')
    else:
        return render(request, 'donate_plasma_form.html')


def donate_plasma(request):
    """
    This method is used to handle plasma donation registration form, it takes data from the form
    and stores it in the database that is for plasma donor.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base, else it will return the donor registration
    form again.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        age = request.POST['age']
        sex = request.POST['sex']
        blood_group = request.POST['blood_group']
        nid = request.POST['nid']
        location = request.POST['location']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        img = request.FILES['image']

        if PlasmaDonate.objects.filter(nid=nid).exists():
            messages.info(request, 'Request Already Exists')
            return render(request, 'donate_plasma_form.html')
        else:

            info = PlasmaDonate(username=request.user.username, first_name=f_name, last_name=l_name, age=age, sex=sex,
                                email=email, nid=nid,
                                blood_type=blood_group,
                                phone_number=contact_number, location=location, image=img)

            info.save()
            return render(request, 'thank_you.html')
    else:
        return render(request, 'donate_plasma_form.html')


def show_plasma_donate_request(request):
    """
     This method is used to display the available plasma donor list.
     :param request: it's a HttpResponse from user.


     :type request HttpResponse.


     :return: this method returns a html page that display all the available entry
     for the plasma donor.


     :rtype: HttpResponse.
     """
    request_list = PlasmaDonate.objects.all()
    return render(request, 'show_plasma_donate_request_list.html', {'request_list': request_list})


def search_donate_request(request):
    """
      This method is used to search plasma donors by blood group, it search all
      the records in the data base for a specific blood group and display the
      results.


      :param request: it's a HttpResponse from user.


      :type request HttpResponse.


      :return: this method returns a html page that display all the available entry
      of the plasma donors in the data base that matches the users entry.


      :rtype: HttpResponse.
      """
    query = request.GET['query']
    if len(query) > 10:
        results = 'X'

    else:
        results = PlasmaDonate.objects.filter(blood_type__icontains=query)

    return render(request, 'search_plasma_donor.html', {'results': results, 'query': query})


def delete_donate_request_form(request):
    """
         This method is used to display the available plasma donor list for a specific
         user and it displays a form for where user can input a id from the list
         to delete that particular plasma donor.


         :param request: it's a HttpResponse from user.


         :type request HttpResponse.


         :return: this method returns a html page. It returns login page when user
          is not logged in, else it returns the page that display form to delete and
          donor list for that specific user.


         :rtype: HttpResponse.
         """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        query = request.user.username
        user_entry = PlasmaDonate.objects.filter(username=query)
        return render(request, 'delete_donate_request_form.html', {'user_entry': user_entry})


def delete_donate_request(request):
    """
        This method is used to handle the delete functionality for plasma donor
        for a specific user. It finds that particular entry of that user and delete
        that entry.


        :param request: it's a HttpResponse from user.


        :type request HttpResponse.


        :return: this method returns the home page for plasma service.


        :rtype: HttpResponse.
        """
    entry = request.POST['query']
    if PlasmaDonate.objects.filter(username=request.user.username, id=entry).exists():
        delete_entry = PlasmaDonate.objects.filter(username=request.user.username, id=entry)
        delete_entry.delete()
        return render(request, 'plasma_home.html')
    else:
        messages.info(request, 'Entry Does Not Exists')
        return render(request, 'delete_request_form.html')
