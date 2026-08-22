from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),
   
]