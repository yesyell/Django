from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def main(request):
    # return HttpResponse("Onememeos~ Hello, World~^.~")
    # return render(request, 'onememos/templates/main.html') X
    # return render(request, 'onememos/main.html') X
    return render(request, 'main.html')

def createMemo(request):
    # request 객체는 사용자가 폼 페이지를 통해 입력한 폼 데이터 값들을 받는다.
    # request.GET, request.POST, request.COOKIE -> 사전형 데이터 -> get, post, cookie 정보들을 받는다.

    # memoContent = request.GET['memoContent']
    memoContent = request.POST['memoContent']

    # DB 입력
    # 만약 DB에 저장이 안된다면 맨 위에서 models.py 파일에서 모든 것을 임포트했는지 체크 ⭐
    # NOT NULL 필드 입력했는지 체크
    # article = Memo(memo_text = memoContent)
    # article.save()

    # return HttpResponse("Create Memo = " + memoContent)
    # -> localhost:8000/onememos/createMemo/?memoContent=대한민국

    # reverse + name 사용하여 리다이렉트
    return HttpResponseRedirect(reverse('main'))