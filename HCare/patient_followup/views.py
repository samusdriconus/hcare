from django.shortcuts import render
from .models import Patient
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
	return render(request, 'home.html')

def patients(request):
    patient_list = Patient.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(patient_list, 10)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    paginator = Paginator(patient_list, 10)
    return render(request, 'patients.html',{'patients':patients})