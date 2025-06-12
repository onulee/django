from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

# form게시판 - get,post
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list.html',context)
    elif request.method == 'POST':
        return render(request,'board/list.html')
        