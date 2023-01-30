from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/onememos/
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),

    # 하나의 요청 -> 2개의 방식(Get vs Post)
    path('writeMemo/', views.writeMemo),
]