from django import forms
from .models import Patient

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'