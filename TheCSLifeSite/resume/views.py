from django.shortcuts import render
from .models import Resume

# Create your views here.
def index(request):

    return render(request, 'resume/index.html', {})
