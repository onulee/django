from django.shortcuts import render
from board.models import Board
from django.db.models import F

# 게시글보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    # 1.qs값 수정
    # qs.bhit += 1
    # qs.save()
    
    # 2.F함수사용 - qs에서 특정컬럼의 값을 가져오는 함수
    qs.update(bhit = F('bhit')+1) #save까지 됨.
    
    context = {'board':qs}
    return render(request,'board/view.html',context)

# 게시판리스트
def list(request):
    # 게시글 전체 가져오기
    qs = Board.objects.order_by('-bgroup','bstep')
    context = {"list":qs}
    return render(request,'board/list.html',context)
