from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def blogs(request):
    context = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': context})
