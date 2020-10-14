from django import template
from  cargotaxi.models import Price

register = template.Library()

@register.simple_tag(name = 'get_list_price')
def get_price():
    return Price.objects.all()