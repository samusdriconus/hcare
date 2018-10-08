from django.shortcuts import render,redirect
from .models import Patient,Appointement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import NewPatientForm,NewAppointementForm
from datetime import datetime, timedelta
# Create your views here.
@login_required
def home(request):
    today = datetime.today().date()
    app_today = Appointement.objects.filter(date=today)
    tomorrow = today + timedelta(days=1)
    app_tomorrow = Appointement.objects.filter(date=tomorrow)
    startweek = today - timedelta(days=today.weekday())
    after_2days = today + timedelta(days=2)
    weekend = startweek + timedelta(days=6)
    week_apps = Appointement.objects.filter(date__range=[after_2days,weekend])

    return render(request, 'home.html',
                    {'today_app':app_today,
                    'tomorrow_app':app_tomorrow,
                    'week_apps' : week_apps
                    })



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
    if request.method == 'POST':
        form = NewAppointementForm(request.POST)
        if form.is_valid():
            appointement = form.save(commit=False)
            appointement.patient = patient
            form.save()
    else:
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



