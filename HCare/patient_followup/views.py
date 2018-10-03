from django.shortcuts import render,redirect
from .models import Patient
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import NewPatientForm,NewAppointementForm

# Create your views here.
@login_required
def home(request):
	return render(request, 'home.html')


@login_required
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


@login_required
def patient_sheet(request, pk):
    patient = Patient.objects.get(pk=pk)
    form = NewAppointementForm()
    return render(request, 'patient.html', {'patient': patient,'form':form})


@login_required
def new_patient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST,request.FILES)
        if form.is_valid():
            patient = form.save()
            return redirect('home')
    else:
        form = NewPatientForm()
    return render(request, 'new_patient.html', {'form': form})



