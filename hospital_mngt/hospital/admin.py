from django.contrib import admin
from .models import Doctor, Patient, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'mobile')
    search_fields = ('name', 'specialization', 'mobile')
    list_filter = ('specialization',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'mobile')
    search_fields = ('name', 'mobile')
    list_filter = ('gender',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'time')
    search_fields = ('doctor__name', 'patient__name', 'date')
    list_filter = ('date', 'doctor')
