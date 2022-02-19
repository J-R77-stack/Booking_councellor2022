from django.contrib import admin
from .models import Appointment
from django.contrib.admin import ModelAdmin


@admin.register(Appointment)
class AppointmentAdmin(ModelAdmin):
    """
    Class to constitute model in admin database.
    """
    list_display = ('user', 'name', 'phone_number', 'email',
                    'appointment_date_and_time')
    search_fields = ('name', 'phone_number', 'email',
                     'appointment_date_and_time')
    list_filter = ('name', 'phone_number', 'email',
                   'appointment_date_and_time')
