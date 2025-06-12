from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

# form게시판 - get,post
def blist(request):
    ### db게시글 전체가져오기
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print('queryset타입 : ',qs)
    ### json타입으로 변경
    l_qs = list(qs.values())
    print('리스트타입 : ',l_qs)
    
    context = {'result':'success','list':l_qs}
    return JsonResponse(context)
    
    
    
