from django.contrib import messages
from django.shortcuts import render
from .models import AvailableAmbulance, ReserveAmbulance, AvailableOxygenCylinder, ReserveOxygenCylinder

"""
Global Variables

"""
a_num = 0
c_num = 0


def emergency_service_provider_home(request):
    """
    This method is used to display home page for this emergency service provider function.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a home page for emergency service providers
     which is a HTML page.


    :rtype: HttpResponse.
    """
    return render(request, 'emergency_service_provider_home.html')


def available_ambulance(request):
    """
     This method is used to display the available ambulance list.


     :param request: it's a HttpResponse from user.


     :type request HttpResponse.


     :return: this method returns a html page that display all the entry
     of the ambulance those are available.


     :rtype: HttpResponse.
     """
    available_ambulance_list = AvailableAmbulance.objects.filter(is_available=True)
    return render(request, 'show_available_ambulance.html', {'available_ambulance_list': available_ambulance_list})


def reserved_ambulance(request):
    """
    This method is used reserve ambulance when user is logged in, else it will
    display the login page for user to log in. It shows a form where user
    have to enter the ambulance number to reserve that particular ambulance and
    also have fill up a form for patient details.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns login page when user
    is not logged in, else it returns the patient information form.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":
            query = request.POST['query']
            global a_num
            ambulance_to_be_reserved = AvailableAmbulance.objects.filter(ambulance_number=query)
            a_num = ambulance_to_be_reserved[0].ambulance_number
            info = ambulance_to_be_reserved[0]
            return render(request, 'ambulance_reserve_form.html', {'info': info})
        else:
            available_ambulance_list = AvailableAmbulance.objects.filter(is_available=True)
            return render(request, 'show_available_ambulance.html',
                          {'available_ambulance_list': available_ambulance_list})


def confirm_reservation(request):
    """
    This method is used to handle the ambulance reservation, it takes data from the
    patient information form and ambulance data and stores it in the database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base, else it will return the ambulance reservation
    form.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        patientname = request.POST['p_name']
        age = request.POST['age']
        sex = request.POST['sex']
        blood_group = request.POST['blood_group']
        nid = request.POST['nid']
        location = request.POST['location']
        contact_number = request.POST['contact_number']
        bkash_number = request.POST['bkash_number']
        bkash_transaction_id = request.POST['bkash_transaction_id']
        hospital_name = request.POST['hospital_name']
        ambulance_type = request.POST['ambulance_type']
        ambulance_number = request.POST['ambulance_number']
        price = request.POST['price']

        if ReserveAmbulance.objects.filter(nid=nid).exists():
            messages.info(request, 'Request Already Exists')
            return render(request, 'ambulance_reserve_form.html')

        else:
            change_database = AvailableAmbulance.objects.get(ambulance_number=a_num)
            change_database.is_available = False

            change_database.save()

            info = ReserveAmbulance(username=request.user.username, hospital_name=hospital_name,
                                    ambulance_type=ambulance_type, ambulance_number=ambulance_number, price=price,
                                    patient_name=patientname, age=age, sex=sex, blood_type=blood_group,
                                    phone_number=contact_number, nid=nid,
                                    location=location, bkash_number=bkash_number,
                                    bkash_transaction_id=bkash_transaction_id)

            info.save()
            return render(request, 'thank_you.html')

    else:
        return render(request, 'ambulance_reserve_form.html')


def search_ambulance(request):
    """
      This method is used to search ambulance by ambulance type, it search all
      the records in the data base for a specific ambulance type and display the
      results.


      :param request: it's a HttpResponse from user.


      :type request HttpResponse.


      :return: this method returns a html page that display all the available entry
      of that ambulance type in the data base that matches the users entry.


      :rtype: HttpResponse.
      """
    query = request.GET['query2']
    if len(query) > 10:
        results = 'X'

    else:
        results = AvailableAmbulance.objects.filter(ambulance_type__icontains=query, is_available=True)

    return render(request, 'search_ambulance.html', {'results': results, 'query': query})


def delete_request_form(request):
    """
      This method is used to display the available ambulance list for a specific
      user and it displays a form for that user where user can input a id from the list
      to delete that particular request for ambulance.


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
        user_entry = ReserveAmbulance.objects.filter(username=query)
        return render(request, 'delete_ambulance_reserve_form.html', {'user_entry': user_entry})


def delete_request(request):
    """
        This method is used to handle the delete functionality for ambulance reservation
        for a specific user. It finds that particular entry of that user and delete
        that entry.


        :param request: it's a HttpResponse from user.


        :type request HttpResponse.


        :return: this method returns the home page for emergency service provider.


        :rtype: HttpResponse.
        """
    entry = request.POST['query']
    if ReserveAmbulance.objects.filter(username=request.user.username, id=entry).exists():
        delete_entry = ReserveAmbulance.objects.get(id=entry)
        temp = delete_entry.ambulance_number
        delete_entry.delete()
        change_database = AvailableAmbulance.objects.get(ambulance_number=temp)
        change_database.is_available = True
        change_database.save()
        return render(request, 'emergency_service_provider_home.html')
    else:
        messages.info(request, 'Entry Does Not Exists')
        return render(request, 'delete_ambulance_reserve_form.html')


def available_oxygen_cylinder(request):
    """
     This method is used to display the available oxygen cylinder list.


     :param request: it's a HttpResponse from user.


     :type request HttpResponse.


     :return: this method returns a html page that display all the entry
     of the oxygen cylinder those are available.


     :rtype: HttpResponse.
     """
    available_oxygen_cylinder_list = AvailableOxygenCylinder.objects.filter(is_available=True)
    return render(request, 'show_available_oxygen_cylinder.html',
                  {'available_oxygen_cylinder_list': available_oxygen_cylinder_list})


def reserved_oxygen_cylinder(request):
    """
    This method is used reserve oxygen cylinder when user is logged in, else it will
    display the login page for user to log in. It shows a form where user
    have to enter the oxygen cylinder number to reserve that particular oxygen cylinder and
    also have fill up a form for patient details.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns login page when user
    is not logged in, else it returns the patient information form.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":
            query = request.POST['query']
            global c_num
            cylinder_to_be_reserved = AvailableOxygenCylinder.objects.filter(cylinder_number=query)
            c_num = cylinder_to_be_reserved[0].cylinder_number
            print(c_num)
            info = cylinder_to_be_reserved[0]
            return render(request, 'oxygen_cylinder_reserve_form.html', {'info': info})
        else:
            available_oxygen_cylinder_list = AvailableOxygenCylinder.objects.filter(is_available=True)
            return render(request, 'show_available_oxygen_cylinder.html',
                          {'available_oxygen_cylinder_list': available_oxygen_cylinder_list})


def confirm_oxygen_reservation(request):
    """
    This method is used to handle the oxygen cylinder reservation, it takes data from the
    patient information form and oxygen cylinder information and stores it in the database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base, else it will return the oxygen reservation form.


    :rtype: HttpResponse.
    """
    if request.method == "POST":
        patientname = request.POST['p_name']
        age = request.POST['age']
        sex = request.POST['sex']
        nid = request.POST['nid']
        location = request.POST['location']
        contact_number = request.POST['contact_number']
        bkash_number = request.POST['bkash_number']
        bkash_transaction_id = request.POST['bkash_transaction_id']
        company_name = request.POST['company_name']
        cylinder_size = request.POST['cylinder_size']
        cylinder_number = request.POST['cylinder_number']
        price = request.POST['price']

        if ReserveOxygenCylinder.objects.filter(nid=nid).exists():
            messages.info(request, 'Request Already Exists')
            return render(request, 'oxygen_cylinder_reserve_form.html')
        else:
            change_database = AvailableOxygenCylinder.objects.get(cylinder_number=c_num)
            change_database.is_available = False

            change_database.save()

            info = ReserveOxygenCylinder(username=request.user.username, company_name=company_name,
                                         cylinder_size=cylinder_size, cylinder_number=cylinder_number, price=price,
                                         patient_name=patientname, age=age, sex=sex, phone_number=contact_number,
                                         nid=nid,
                                         location=location, bkash_number=bkash_number,
                                         bkash_transaction_id=bkash_transaction_id)

            info.save()
            return render(request, 'thank_you.html')

    else:

        return render(request, 'oxygen_cylinder_reserve_form.html')


def search_oxygen_cylinder(request):
    """
      This method is used to search oxygen cylinder by cylinder size, it search all
      the records in the data base for a specific cylinder size and display the
      results.


      :param request: it's a HttpResponse from user.


      :type request HttpResponse.


      :return: this method returns a html page that display all the available entry
      of that cylinder size in the data base that matches the users entry.


      :rtype: HttpResponse.
      """
    query = request.GET['query2']
    if len(query) > 10:
        results = 'X'

    else:
        results = AvailableOxygenCylinder.objects.filter(cylinder_size__icontains=query, is_available=True)

    return render(request, 'search_oxygen.html', {'results': results, 'query': query})


def delete_oxygen_request_form(request):
    """
      This method is used to display the reserved oxygen cylinder list for a specific
      user and it displays a form for that user where user can input a id from the list
      to delete that particular request for oxygen cylinder.


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
        user_entry = ReserveOxygenCylinder.objects.filter(username=query)
        return render(request, 'delete_oxygen_reserve_form.html', {'user_entry': user_entry})


def delete_oxygen_request(request):
    """
        This method is used to handle the delete functionality for oxygen cylinder reservation
        for a specific user. It finds that particular entry of that user and delete
        that entry.


        :param request: it's a HttpResponse from user.


        :type request HttpResponse.


        :return: this method returns the home page for emergency service provider.


        :rtype: HttpResponse.
        """

    entry = request.POST['query']

    if ReserveOxygenCylinder.objects.filter(username=request.user.username, id=entry):
        delete_entry = ReserveOxygenCylinder.objects.get(id=entry)
        temp = delete_entry.cylinder_number
        delete_entry.delete()
        change_database = AvailableOxygenCylinder.objects.get(cylinder_number=temp)
        change_database.is_available = True
        change_database.save()
        return render(request, 'emergency_service_provider_home.html')
    else:
        messages.info(request, 'Entry Does Not Exists')
        return render(request, 'delete_oxygen_reserve_form.html')
