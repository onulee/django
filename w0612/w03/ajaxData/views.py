from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board


# bwrite 글쓰기
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print('html에서 server측으로 전달데이터 : ',id,btitle,bcontent)
    
    context = {'result':'success'}
    return JsonResponse(context)
