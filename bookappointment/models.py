from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appointment(models.Model):
    """
    class for appointment model in database and for
    the appointment form.
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    appointment_date_and_time = models.DateTimeField(null=True)
    phone_number = models.CharField(null=True, blank=True, max_length=16)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name', 'appointment_date_and_time')
        ordering = ['-created_on']

    def _str_(self):
        """
        Function to return model items as a string"
        """
        return f'User {self.user} has made an appointment \
                  for {self.name} \
                  for {self.appointment_date_and_time}.'    