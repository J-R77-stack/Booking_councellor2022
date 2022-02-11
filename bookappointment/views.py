from django.shortcuts import render
from .models import Appointment


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


def view_contact(request):
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



