from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from .models import Patient, TreatmentLog, Appointment
from .serializers import PatientSerializer, TreatmentLogSerializer, AppointmentSerializer
from .forms import PatientForm

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class TreatmentLogViewSet(viewsets.ModelViewSet):
    queryset = TreatmentLog.objects.all()
    serializer_class = TreatmentLogSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-appointment_date')
    serializer_class = AppointmentSerializer


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinic/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinic/patient_form.html', {'form': form})
