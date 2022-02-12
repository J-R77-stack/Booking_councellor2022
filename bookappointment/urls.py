from django.urls import path
from bookappointment import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('services/', views.view_services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.view_about, name='about'),   
    path('blog/', views.view_blog, name='blog'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('edit_appointment/', views.edit_appointment, name='edit_appointment'),
    path('delete/<appointment_id>', views.delete_appointment, name='delete_appointment'),
]