from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import AvailableICU, BookingICU ,AvailableHospitalBed,BookingHospitalBed
from django.http import HttpResponse

global_veriable = 0;
global_veriable2 = 0;

def reserve_page(request):
    """
    This method is used to show the selection page of see available ICU and see available hospital bed.
    by clicking one of the option it shows the corresponding page.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page.It returns a page where it has two options.one is see available
    ICU and see available hospital base pages.


    :rtype: HttpResponse.
    """
    return render(request, 'Reserve_Page.html')


def available_icu(request):
    """
    This method is used to display the available ICU list.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page that display all the available entry
    of the ICU.


    :rtype: HttpResponse.
    """
    available_icu_ver = AvailableICU.objects.all()
    return render(request, 'Available_ICU.html', {'available_icu_ver': available_icu_ver})

def see_reserve_icu(request):
    """
    This method is used to display the reserved ICU list of that specific user.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page that display all the reserved ICU list if the user is
    logged in. else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        see_reserve_icu_ver = BookingICU.objects.all()
        return render(request, 'See_Reserved_ICU.html', {'see_reserve_icu_ver': see_reserve_icu_ver})

def see_reserved_hospital_bed(request):
    """
    This method is used to display the reserved Hospital bed list of that specific user.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page that display all the reserved ICU list if the user is logged in.
    else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        see_reserved_hospital_bed_ver = BookingHospitalBed.objects.all()
        return render(request, 'See_Reserved_Hospital_Bed.html', {'see_reserved_hospital_bed_ver': see_reserved_hospital_bed_ver})



def deleted_icu(request):
    """
    This method is used to delete the specific reserved ICU entry by ID and it changes the availability
    of that specific ICU entry in the available ICU database.finally it shows the confirmation of delete page.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns the page of confirmation of delete if the user is logged in.
    else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        delete_id = request.POST['ID_Number']
        new_delete_id = int(delete_id)
        deleted_icu_ver = BookingICU.objects.get(id=new_delete_id)
        previous_id = deleted_icu_ver.previous_id
        deleted_icu_ver.delete()
        change_in_database = AvailableICU.objects.get(id=previous_id)
        change_in_database.is_available = "1"
        change_in_database.save()
        return render(request, 'Deleted_From_ICU.html')

def deleted_hospital_bed(request):
    """
    This method is used to delete the specific reserved hospital bed entry by ID and it changes the availability
    of that specific hospital bed entry in the available hospital bed database.finally it shows the confirmation of delete page.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns the page of confirmation of delete if the user is logged in.
    else it will return the log in page.


    :rtype: HttpResponse.
    """
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        delete_id = request.POST['ID_Number']
        new_delete_id = int(delete_id)
        deleted_hospital_bed_ver = BookingHospitalBed.objects.get(id=new_delete_id)
        previous_id = deleted_hospital_bed_ver.previous_id
        deleted_hospital_bed_ver.delete()
        change_in_database = AvailableHospitalBed.objects.get(id=previous_id)
        change_in_database.is_available = "1"
        change_in_database.save()
        return render(request, 'Deleted_From_Hospital_Bed.html')

def available_hospital_bed(request):
    """
    This method is used to display the available hospital bed list.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page that display all the available entry
    of hospital bed.


    :rtype: HttpResponse.
    """
    available_hospital_bed_ver = AvailableHospitalBed.objects.all()
    return render(request, 'Available_Hospital_Bed.html', {'available_hospital_bed_ver': available_hospital_bed_ver})


def confirm_booking_for_hospital_bed(request):
    """
    This method is used to handle the hospital bed reservation, it takes data from the
    patient information form and confirm payment.finally it stores the hospital bed
    information and payment confirmations in the database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a form page of the patient details and payment confirmation page
    of hospital bed. if the input is wrong it will show a wrong id massage.


    :rtype: HttpResponse.
    """
    global global_veriable2
    available_hospital_bed_ver = AvailableHospitalBed.objects.all()
    id = request.POST['ID_Number']
    check_availability = AvailableHospitalBed.objects.get(id=id)
    new_id = int(id)-1
    if check_availability.is_available == "1":
        info = available_hospital_bed_ver[new_id]
        global_veriable2 = new_id
        global_veriable2 = global_veriable2 + 1
        return render(request, 'Confirm_Booking_For_Hospital_Bed.html', {'info': info})
    else:
        return HttpResponse("Wrong ID")

def confirm_booking_icu(request):
    """
    This method is used to handle the ICU reservation, it takes data from the patient information
    form and confirm payment.finally it stores the ICU information and payment confirmations in the database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a form page of the patient details and payment confirmation page
    of ICU. if the input is wrong it will show a wrong id massage.


    :rtype: HttpResponse.
    """

    global global_veriable
    available_icu_ver = AvailableICU.objects.all()
    id = request.POST['ID_Number']
    check_availability = AvailableICU.objects.get(id=id)
    new_id = int(id) - 1
    if check_availability.is_available == "1":
        info = available_icu_ver[new_id]
        global_veriable = new_id
        global_veriable = global_veriable + 1
        return render(request, 'Confirm_Booking.html', {'info': info})
    else:
        return HttpResponse("Wrong ID")


def thank_you(request):
    """
    This method is used to handle the request of confirm reservation of ICU page, it takes data from the form and modify
    the availability of that specific entry of the available ICU database and stores it in the booking ICU database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base.


    :rtype: HttpResponse.
    """
    change_in_database = AvailableICU.objects.get(id=global_veriable)
    change_in_database.is_available = "0"
    change_in_database.save()
    if request.method == "POST":
        patient_name = request.POST['Patient_Name']
        patient_blood_group = request.POST['Patient_Blood_Group']
        patient_age = request.POST['Patient_Age']
        contact_number = request.POST['Contact_Number']
        bkash_number = request.POST['Bkash_Number']
        bkash_transaction_id = request.POST['Bkash_Transaction_ID']
        hospital_name = request.POST['Hospital_Name']
        icu_type = request.POST['ICU_Type']
        price = request.POST['Price']
        is_available = request.POST['Is_Available']
        print(hospital_name, icu_type, price, is_available)
        ins = BookingICU(user_name=request.user.username, email=request.user.email, contact_number=contact_number, patient_age=patient_age, patient_name=patient_name, patient_blood_group=patient_blood_group, bkash_number=bkash_number, bkash_transaction_id=bkash_transaction_id, hospital_name=hospital_name, icu_type=icu_type, price=price, is_available=is_available, previous_id=global_veriable)
        ins.save()
    return render(request, "Thank_You.html")

def thank_you_for_hospital_bed(request):
    """
    This method is used to handle the request of confirm reservation of hospital bed page, it takes data from the form and modify
    the availability of that specific entry of the available hospital bed database and stores it in the booking hospital bed database.


    :param request: it's a HttpResponse from user.


    :type request HttpResponse.


    :return: this method returns a html page. It returns a thank you page when data
    is successfully stored in data base.


    :rtype: HttpResponse.
    """
    change_in_database = AvailableHospitalBed.objects.get(id=global_veriable2)
    change_in_database.is_available = "0"
    change_in_database.save()
    if request.method == "POST":
        patient_name = request.POST['Patient_Name']
        patient_blood_group = request.POST['Patient_Blood_Group']
        patient_age = request.POST['Patient_Age']
        contact_number = request.POST['Contact_Number']
        available_ac = request.POST['Available_AC']
        bkash_number = request.POST['Bkash_Number']
        bkash_transaction_id = request.POST['Bkash_Transaction_ID']
        hospital_name = request.POST['Hospital_Name']
        bed_number = request.POST['Bed_Number']
        price_per_day = request.POST['Price_Per_Day']
        is_available = request.POST['Is_Available']
        ins = BookingHospitalBed(user_name=request.user.username, email=request.user.email, contact_number=contact_number ,available_ac=available_ac , patient_age=patient_age, patient_name=patient_name, patient_blood_group=patient_blood_group, bkash_number=bkash_number, bkash_transaction_id=bkash_transaction_id, hospital_name=hospital_name, bed_number=bed_number, price_per_day=price_per_day, is_available=is_available, previous_id=global_veriable2)
        ins.save()
    return render(request, "Thank_You_For_Hospital_Bed.html")

