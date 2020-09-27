from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

# @desc Blog Page
# @route http://127.0.0.1:8000/blog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})
