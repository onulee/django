from django.shortcuts import render,redirect
from django.http import JsonResponse
from board.models import Board

def list3(request):
    return render(request,'board/list3.html')

#--------------------------------------------------

def view2(request,bno):
    print(bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view2.html',context)


# from - get,post
def list2(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list2.html',context)
    elif request.method == 'POST':
        return render(request,'board/list2.html')

#-------------------------------------------------

def view(request):
    bno = request.GET.get('bno')
    print('넘어온 bno : ',bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)

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
        