from django.shortcuts import render,redirect
from django.http import JsonResponse
from board.models import Board

# form게시판 - get,post
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print("넘어온 데이터 : ",id,btitle,bcontent)
        
        # db저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        
        return redirect("/board/list/")
        