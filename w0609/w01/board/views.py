from django.shortcuts import render
from django.core.paginator import Paginator
from board.models import Board

## 글쓰기 - get,post
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        return render(request,'board/write.html')
        

## 게시판리스트
def list(request):
    # 페이지번호가 있어야 함.
    page = int(request.GET.get('page',1))
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    # 하단넘버링부분
    paginator = Paginator(qs,10)    # 10개씩 분리해서 가져옴. 1,2,...10페이지생성
    list = paginator.get_page(page) # 1페이지 가져오기 -> 10개 게시글
    # -----------
    context = {'list':list,'page':page}
    return render(request,'board/list.html',context)
