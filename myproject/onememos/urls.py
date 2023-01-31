from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/onememos/
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),

    # 하나의 요청 -> 2개의 방식(Get vs Post)
    path('writeMemo/', views.writeMemo),

    # 수정 처리 요청
    path('edit/<str:idx>', views.editPage),
]