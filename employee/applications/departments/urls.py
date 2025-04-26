from django.contrib import admin
from django.urls import path
from .views import NewDepartmentView

urlpatterns = [
    path('new/',NewDepartmentView.as_view(),name='new'),
]