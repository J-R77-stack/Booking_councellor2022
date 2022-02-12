from .models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'phone_number', 'email', 'appointment_date_and_time')
