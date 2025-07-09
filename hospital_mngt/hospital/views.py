from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor
from .forms import DoctorForm  
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
#from .forms import DoctorForm


@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

@login_required
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospital/doctor_form.html', {'form': form})

@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'hospital/doctor_form.html', {'form': form})

@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'hospital/doctor_confirm_delete.html', {'doctor': doctor})



def about_view(request):
    return render(request, 'about.html')

def home_view(request):
    services = [
        "Emergency", "Pharmacy", "USG", "Endoscopy", "ECHO Services",
        "Colonoscopy", "Digital X-Ray", "Lab", "Coloscopy"
    ]
    return render(request, 'home.html', {'services': services})

def contact_view(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def index_view(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have access to the admin dashboard.")
        return redirect('login')
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials or insufficient permissions.")

    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_create.html', {'form': form})