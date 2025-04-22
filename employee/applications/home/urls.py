from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', InderView.as_view()),
    path('list/', PruebaListView.as_view()),
    path('lista-prueba/', ModeloPrueba.as_view()),
    path('add/', PruebaCreateView.as_view(),name="add"),
]