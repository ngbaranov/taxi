from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Home, Service, Price, ApplForms

class ViewHome(ListView):
    model = Home
    template_name = 'cargotaxi/index.html'
    context_object_name = 'home'

class ViewService(ListView):
    model = Service
    template_name = 'cargotaxi/service.html'
    context_object_name = 'service'



# Create your views here.
