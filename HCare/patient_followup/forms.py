from django import forms
from .models import Patient,Appointement
from datetimepicker.widgets import DateTimePicker
class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'picture' : forms.FileInput(attrs={'multiple': False})
        }
    

class NewAppointementForm(forms.ModelForm):
    class Meta:
        model = Appointement
        fields = ["date","duration","note"]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'date'}),
        }
    



      