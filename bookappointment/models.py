from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    """
    class for appointment model in database and for
    the appointment form.
    """
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    appointment_date_and_time = models.DateTimeField(null=True)

    def validate_date(appointment_date_and_time):
        if appointment_date_and_time < timezone.now():
            raise ValidationError('Booking date is not available, please try again')

    appointment_date_and_time = models.DateTimeField(null=True, blank=True,
                                                     validators=[validate_date]
                                                     )
    phone_number = models.CharField(null=True, blank=True, max_length=16)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name', 'appointment_date_and_time')
        ordering = ['-created_on']
