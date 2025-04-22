from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Employee

# Create your views here.
class ListAllEmployee(ListView):
    template_name = 'employees/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
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

class ListSkillView(ListView):
    template_name = 'employees/list_skills.html'
    context_object_name = 'skills'
    def get_queryset(self):
        key = int(self.request.GET.get('kword', ''))
        #print(type(int(key)))
        person = Employee.objects.get(id=key)
        data = []
        data.append(person.first_name +' '+ person.second_name)
        for skill in person.skills.all():
            data.append(str(skill).split('-').pop())
            print(data)
        #print(data.pop(0))
        return data


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/person.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
   template_name = "employees/success.html"




class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employees/register.html"
    fields = ['first_name','second_name','job','department','skills']
    #fields = ('__all__')
    success_url = reverse_lazy('persona_app:success')

    def form_valid(self, form):
        #worker = form.save()
        worker = form.save(commit=False)
        worker.full_name = worker.first_name + ' ' + worker.second_name
        worker.save()
        return super(EmployeeCreateView,self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/update.html'
    fields = ['first_name','second_name','job','department','skills']
    success_url = reverse_lazy('persona_app:success')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super(EmployeeUpdateView,self).form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employees/delete.html"
    success_url = reverse_lazy('persona_app:success')

