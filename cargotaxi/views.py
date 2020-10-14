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

# def price(request):
#     return render(request,'cargotaxi/price.html')

class ViewPrice(DetailView):
    model = Price
    template_name = 'cargotaxi/price.html'
    context_object_name = 'view_price'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['price_one'] = Price.objects.get(pk= 1)
    #     return context



# Create your views here.
