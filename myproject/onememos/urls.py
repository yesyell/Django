from django.urls import path

from . import views

urlpattterns = [
    path('', views.index, name='index'),

]