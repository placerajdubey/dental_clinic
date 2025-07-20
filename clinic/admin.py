from django.contrib import admin
from .models import Patient, Appointment, TreatmentLog

#admin.site.register(Patient)

# Register your models here. to customize the admin interface for Patient model

class TreatmentInline(admin.TabularInline):
    model = TreatmentLog
    extra = 1

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('gender',)
    readonly_fields = ('xray_image', 'prescription_file')
    inlines = [TreatmentInline]  # 👈 Add treatment log inline

admin.site.register(Appointment)

admin.site.register(TreatmentLog)
