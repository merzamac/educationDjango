from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee

# Create your views here.
class ListAllEmployee(ListView):
    template_name = 'employees/list_all.html'
    model = Employee

class ListByArea(ListView):
    template_name = 'employees/list_area.html'
    """queryset = Employee.objects.filter(
        department__short_name = 'contabilidad'
    )"""

    def get_queryset(self):
        area = self.kwargs['shortname']
        list = Employee.objects.filter(
        department__short_name = area
        )
        return list

class GetEmployeeByKword(ListView):
    template_name = 'employees/by_kword.html'
    context_object_name =  'data'

    def get_queryset(self):
        key = self.request.GET.get('kword','')
        #print(key)
        return Employee.objects.filter(
        first_name = key
        )
