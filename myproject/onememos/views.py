from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# render 함수와 template 파일의 관계
#   - 웹사이트 개발 시 파이썬 코드와 데이터를 템플릿 파일로 만들어주는 함수(HTML로 변환해서 적용)
#   - HTML 파일로 리턴한 것 -> 템플릿(Template) 또는 템플릿 파일
#   - 그러나 템플릿 파일이 HTML 파일은 아니다.
#   - 이러한 템플릿 파일은 대부분의 프레임워크에서도 마찬가지인데 프레임워크 전용 파일의 개념
#   - 장고에서만 사용할 수 있는 문법(또는 태그) 등을 이러한 템플릿에 적용 -> 일반 HTML 파일 X
#   - 템플릿도 규칙과 최소한의 문법(템플릿 태그)이 존재
#   - 조건 처리, 반복 처리 등이 가능 -> 템플릿 전용 표현 언어

# 템플릿 폴더 만들기
#   1. 프로젝트 루트 폴더에 templates 폴더를 만들어서 사용 → settings.py → 템플릿 경로 추가하여 사용
#   2. 생성한 앱(App)쪽 바로 하위에 templates 폴더를 만들어서 사용 → 앱별로 템플릿 사용 가능 ✅
#   -> 즉, 장고는 템플릿 폴더를 인식하는 방식이 여러 가지
#   - onememos 앱의 경우 하위에 template 폴더 생성하면 별다른 설정 없이 바로 템플릿 디렉토리 인식
#   - python manage.py runserver 서버 재시작 ⭐️

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
    article = Memo(memo_text = memoContent)
    article.save()

    return HttpResponse("Create Memo = " + memoContent)
    # localhost:8000/onememos/createMemo/?memoContent=대한민국