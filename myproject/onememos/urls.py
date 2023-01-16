from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/onememos/
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),
]