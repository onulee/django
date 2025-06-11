from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from member.models import Member
from board.models import Board
from comment.models import Comment

def list(request):
    # id = request.session['session_id'] # 로그인이 되어 있어야 하단댓글 가능
    id = 'aaa'
    member = Member.objects.get(id=id)
    bno = request.POST.get('bno',1)
    board = Board.objects.get(bno=bno)
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent','')
    print("넘어온 데이터 : ",member,board,cpw,ccontent)
    # QuerySet타입 -> list타입
    qs = Comment.objects.create(board=board,member=member,cpw=cpw,
                                 ccontent=ccontent)
    
    print('qs : ',qs) # ok
    
    # filter 리스트타입으로 리턴
    list_qs = list(Comment.objects.filter(cno=qs.cno).values())
    print('list_qs : ',list_qs)
    context = {'result':'success','comment':qs,'comment_list':list_qs}
    
    return JsonResponse(context)
