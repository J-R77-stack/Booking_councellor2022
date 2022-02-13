from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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





@login_required
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
            messages.success(request, 'Appointment booked successfully.')
            return redirect('view_appointment')
        else: 
            messages.error(request, 'Booking date is not available.')
         
    form = AppointmentForm()
    context = {
        'form': form
    }

    return render(request, 'add_appointment.html', context)    

@login_required
def view_appointment(request):
    """
    Function allows user to view an appointment 
    after it's been added to the database.
    """
    appointments = Appointment.objects.filter(user__in=[request.user]) 
    context = {
        'appointments': appointments
    }  
    return render(request, 'view_appointment.html', context)



@login_required
def edit_appointment(request, appointment_id):
    """
    Function allows user to edit an appointment 
    after it's been added to the database.
    """
    appoint = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appoint)
        if form.is_valid():
             appointment = form.save()
             appointment.user = request.user
             appointment.save()
             messages.success(request, 'Your appointment has been updated.')
        return redirect('view_appointment')
    form = AppointmentForm(instance=appoint)
    context = {
        'form': form
    }
    return render(request, 'edit_appointment.html', context)   
    

@login_required
def delete_appointment(request, appointment_id):
    """
    Function allows user to delete an appointment 
    after it's been added to the database.
    """ 
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if appointment.delete():
            messages.success(request, 'Your appointment has been deleted.')
            return redirect('view_appointment')
    form = AppointmentForm(instance=appointment)
    context = {
        'form': form
    }
    return render(request, 'delete_appointment.html', context) 

    
    