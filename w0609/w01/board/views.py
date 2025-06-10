from django.shortcuts import render
from board.models import Board

## 게시판리스트
def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request,'board/list.html',context)
