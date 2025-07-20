from rest_framework import serializers
from .models import Patient, TreatmentLog, Appointment

class TreatmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentLog
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    treatments = TreatmentLogSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.name')

    class Meta:
        model = Appointment
        fields = '__all__'