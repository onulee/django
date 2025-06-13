from django.shortcuts import render
from django.http import JsonResponse

## 하단등록 - Json타입리턴
def cwrite(request):
    # html에서 디장고로 데이터 전달
    id = request.POST.get('id')
    cpw = request.POST.get('cpw')
    ccontent = request.POST.get('ccontent')
    print('넘어온 데이터 : ',id,cpw,ccontent)
    
    context = {'result':'success'}
    return JsonResponse(context)


## 하단댓글리스트 - Json타입리턴
def clist(request):
    context = {'result':'success'}
    return JsonResponse(context)
