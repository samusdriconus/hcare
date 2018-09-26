from django.shortcuts import render
from .models import Patient

# Create your views here.

def home(request):
	return render(request, 'home.html')

def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html',{'patients':patients})