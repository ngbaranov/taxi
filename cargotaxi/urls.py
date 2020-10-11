from django.urls import path
from .views import *

urlpatterns = [
 path('', ViewHome.as_view(), name='home'),
 path('service/', ViewService.as_view(), name='service')
]