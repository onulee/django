from django.shortcuts import render
from board.models import Board

# 쓰기페이지, 쓰기 저장
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        print('데이터 확인 : ',btitle,bcontent,bfile)
        print('데이터추가 : ',qs.bgroup,qs.bstep,bfile)
        return render(request,'board/write.html')
        

# 게시판리스트
def list(request):
    return render(request,'board/list.html')
