from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def main(request):
    return HttpResponse("Onememeos~ Hello, World~^.~")

def createMemo(request):
    # request 객체는 사용자가 폼 페이지를 통해 입력한 폼 데이터 값들을 받는다.
    # request.GET, request.POST, request.COOKIE
    # --> 사전형 데이터 --> get, post, cookie 정보들을 받는다.
    memoContent = request.GET['memoContent']
    return HttpResponse("Create Memo = " + memoContent)