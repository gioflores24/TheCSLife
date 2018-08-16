from django.shortcuts import render
from .models import Resume


# Create your views here.
def index(request):
    resumes = Resume.objects.all()
    return render(request, 'resume/index.html', {'resumes': resumes})
