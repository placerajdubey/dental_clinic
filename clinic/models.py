from django.db import models

from django.db import models

def upload_to(instance, filename):
    return f'uploads/patients/{instance.name}/{filename}'

# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)

    medical_history = models.TextField(blank=True, help_text="Include allergies, conditions, etc.")
    xray_image = models.FileField(upload_to=upload_to, blank=True, null=True)
    prescription_file = models.FileField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

# Treatment Log Model
class TreatmentLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatments')
    treatment_date = models.DateField()
    procedure = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    charges = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.patient.name} - {self.procedure} on {self.treatment_date}"
