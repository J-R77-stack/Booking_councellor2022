from django.urls import path
from bookappointment import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('services/', views.view_services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.view_about, name='about'),   
    path('blog/', views.view_blog, name='blog'),
]