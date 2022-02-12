from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm


def view_home(request):
    """
    Function allows user to view the home page
    """
    return render(request, 'index.html')


def view_services(request):
    """
    Function allows user to view the services page
    """
    return render(request, 'services.html')


def contact(request):
    """
    Function allows user to view the contact page
    """
    return render(request, 'contact.html')


def view_about(request):
    """
    Function allows user to view the about page
    """
    return render(request, 'about.html')


def view_blog(request):
    """
    Function allows user to view the blog page
    """
    return render(request, 'blog.html')


def add_appointment(request):
    """
    Function allows user to make an appointment
    and add appointment to database.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.user = request.user
            appointment.save()
            return redirect('view_appointment')
        else: form = AppointmentForm() 
    
    context = {
        'form': form
    }

    return render(request, 'add_appointment.html', context)    



