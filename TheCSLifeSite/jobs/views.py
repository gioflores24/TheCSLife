from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    context = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs':context})