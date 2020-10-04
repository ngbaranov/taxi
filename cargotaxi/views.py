from django.shortcuts import render
from django.views.generic import ListView
from .models import Home

class ViewHome(ListView):
    model = Home
    template_name = 'cargotaxi/index.html'
    context_object_name = 'home'


# Create your views here.
