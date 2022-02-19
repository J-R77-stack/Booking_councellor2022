from .models import Appointment
from django import forms
from tempus_dominus.widgets import DateTimePicker


class AppointmentForm(forms.ModelForm):
    """
    Class to render the appointment form from the model
    """
    class Meta:
        model = Appointment
        fields = ('name', 'phone_number', 'email', 'appointment_date_and_time')

    def __init__(self, *args, **kwargs):
        """
        Add class, required field and DateTime picker
        to fourth field.
        """
        super().__init__(*args, **kwargs)
        self.fields['appointment_date_and_time'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['appointment_date_and_time'].widget = DateTimePicker()
        self.fields['appointment_date_and_time'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['required'] = 'required'
