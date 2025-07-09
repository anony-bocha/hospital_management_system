from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"


class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.gender})"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.date} at {self.time}"

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
