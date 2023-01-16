from django.contrib import admin
from django.urls import path, include

# urlpatterns 정리
#       - 슬래시(/) 붙이기
#       - 서버 구동 시 변화가 감지되면 자동으로 리로더
#       - 초기화면 views.index 또는 views.main
urlpatterns = [
    path("admin/", admin.site.urls),
    path('onememos/', include('onememos.urls')),
]
