from django import forms
from .models import Doctor
#from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'mobile', 'address']  # adjust fields to your Patient model

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'mobile', 'specialization'] 