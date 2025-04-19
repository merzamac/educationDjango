from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import  *
# Create your views here.
class InderView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    template_name = 'home/list.html'
    queryset = ['prueba1', 'prueba2', 'prueba3']
    context_object_name = 'pruebas'

class ModeloPrueba(ListView):
    model = Prueba
    template_name = 'home/prueba.html'
    context_object_name = 'lista_prueba'
