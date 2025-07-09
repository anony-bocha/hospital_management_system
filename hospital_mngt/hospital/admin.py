from django.contrib import admin
from .models import Doctor, Patient, Appointment






@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'phone', 'specialization', 'email', 'created_at')
    search_fields = ('name', 'specialization', 'email')
    list_filter = ('gender', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'mobile', 'created_at')
    search_fields = ('name', 'mobile')
    list_filter = ('gender',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'time', 'created_at')
    search_fields = ('doctor__name', 'patient__name', 'date')
    list_filter = ('doctor', 'date')
