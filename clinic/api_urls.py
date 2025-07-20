from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TreatmentLogViewSet, AppointmentViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('treatments', TreatmentLogViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = router.urls
