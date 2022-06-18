from django.urls import path
from . import views

#list of urls
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),
]