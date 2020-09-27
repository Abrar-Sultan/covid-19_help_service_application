from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

# @desc Blog Page
# @route http://127.0.0.1:8000/blog


def blog(request):
    """
    :param request: request
    :return: all the blog items in blogs as dictionary object to be rendered
    """
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})
