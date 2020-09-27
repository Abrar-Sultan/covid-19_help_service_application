from django.shortcuts import render
from django.http import HttpResponse


def request_plasma(request):
    return render(request, 'request_plasma_form.html')
