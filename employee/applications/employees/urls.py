from django.contrib import admin
from django.urls import path
from .views import *

app_name = "persona_app"
urlpatterns = [
    path('list_all/', ListAllEmployee.as_view()),
    path('list_area/<shortname>/', ListByArea.as_view()),
    path('by_kword/', GetEmployeeByKword.as_view()),
    path('list_skills/', ListSkillView.as_view()),
    path('person/<pk>', EmployeeDetailView.as_view()),
    path('register/', EmployeeCreateView.as_view()),
    path('success/', SuccessView.as_view(),name='success'),
    path('update/<pk>/', EmployeeUpdateView.as_view(), name='update'),
    path('delete/<pk>/', EmployeeDeleteView.as_view(), name='delete'),

]