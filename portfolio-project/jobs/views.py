from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
  #  All job objects inside DB by saying the name of the class.   
  jobs = Job.objects
  return render(request, 'jobs/home.html', {'jobs': jobs})

#urls.py asks for a job_id, so this must be forwarded
def detail(request, job_id):
  job_detail = get_object_or_404(Job, pk=job_id)
  return render(request, 'jobs/detail.html', {'job':job_detail})
