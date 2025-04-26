from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartmentForm
from applications.employees.models import Employee
from .models import Department

# Create your views here.
class NewDepartmentView(FormView):
    template_name = 'department/new.html'
    form_class = NewDepartmentForm
    success_url = '/'

    def form_valid(self, form):
        print('estamos en ')
        depa = Department(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Employee.objects.create(
            first_name = nombre,
            second_name = apellido,
            job='1',
            department = depa        )
        return super(NewDepartmentView,self).form_valid(form)