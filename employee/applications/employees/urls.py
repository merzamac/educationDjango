from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('list_all/', ListAllEmployee.as_view()),
    path('list_area/<shortname>/', ListByArea.as_view()),
    path('by_kword/', GetEmployeeByKword.as_view()),
]