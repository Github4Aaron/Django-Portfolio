from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
  #  All job objects inside DB by saying the name of the class.   
  jobs = Job.objects
  return render(request, 'jobs/home.html', {'jobs': jobs})
