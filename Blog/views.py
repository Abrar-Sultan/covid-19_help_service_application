from django.shortcuts import render
from django.http import HttpResponse

# @desc Blog Page
# @route http://127.0.0.1:8000/blog


def blog(request):
    return HttpResponse('<h1> This is the Blog App! <h1>')
