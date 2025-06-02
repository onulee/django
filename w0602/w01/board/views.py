from django.shortcuts import render,redirect
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
        # DB저장후 qs변수로 다시 리턴받음.
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        print('데이터 확인 : ',btitle,bcontent,bfile)
        print('데이터추가 : ',qs.bgroup,qs.bstep,bfile)
        return redirect('board:list')
        

# 게시판리스트
def list(request):
    # 모든 데이터 가져오기
    qs = Board.objects.order_by('-bno')
    context = {'list':qs}
    return render(request,'board/list.html',context)
