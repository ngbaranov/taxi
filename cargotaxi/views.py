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

class ViewPrice(DetailView):
    model = Price
    template_name = 'cargotaxi/price.html'
    context_object_name = 'price'



# Create your views here.
