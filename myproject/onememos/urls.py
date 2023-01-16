from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/onememos/ ## 기본 주소
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),
]