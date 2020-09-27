from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ConsultWithDoctor


def doctor(request):
    """
    :param request: request
    :return: renders the basic view of index.html for consultWithDoctors page
    """
    return render(request, 'consult_doctor.html')

