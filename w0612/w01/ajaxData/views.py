from django.shortcuts import render
from django.http import JsonResponse
# form게시판 - get,post
def blist(request):
    context = {'result':'success'}
    return JsonResponse(context)
    
    
    
