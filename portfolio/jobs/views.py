from django.shortcuts import render, get_object_or_404
from .models import job
# Create your views here.


def homepage(request):
    jobs = job.objects.all()
    return render(request, 'jobs/home.html', {'jobs':jobs})

def details(request,job_id):
    print(job_id)
    job_obj = get_object_or_404(job,pk=job_id)
    return render(request,'jobs/details.html',{'job':job_obj})