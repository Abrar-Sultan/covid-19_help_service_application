from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ConsultWithDoctor


def index(request):
    """
    :param request: request
    :return: renders the basic view of index.html for consultWithDoctors page
    """
    return render(request, 'index.html')

