from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers # json타입으로 변경
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리

# form게시판 - get,post
def list(request):
    return render(request,'board/list.html')
    