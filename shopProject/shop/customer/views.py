from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from customer.models import Customer
from member.models import Member

# 게시글 상세보기
def view(request,bno):
    qs = Customer.objects.get(bno=bno)
    context = {'customer':qs}
    return render(request,'customer/view.html',context)

# 게시글 쓰기 - get:글쓰기페이지, post:글쓰기저장
def write(request):
    if request.method == 'GET':
        return render(request,'customer/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        ## session 서버 
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        bfile2 = request.FILES.get('bfile2','')
        qs = Customer.objects.create(btitle=btitle,member=member,bcontent=bcontent,bfile=bfile,bfile2=bfile2)
        qs.bgroup = qs.bno
        qs.save()
        print('------------------')
        print(btitle,id,bcontent,bfile,bfile2)
        print('------------------')
        context = {'msg':1}
        return render(request,'customer/write.html',context)
        return render(request,'customer/write.html',context)
        

# 게시판리스트
def list(request):
    # 요청하는 page번호 가져오기, str타입 -> int타입
    page = int(request.GET.get('page',1))
    # db에서 데이터 가져오기
    qs = Customer.objects.all().order_by('-ntchk','-bgroup','bstep')
    # 10개단위로 qs로 분리시킴
    paginator = Paginator(qs,10)
    
    # 가져올 페이지 선택
    customerList = paginator.get_page(page)
    print('-----------------')
    print(customerList)
    print('-----------------')
    
    # 게시글 10개, 현재페이지 보냄
    context = {'list':customerList,'page':page}
    return render(request,'customer/list.html',context)
    # return redirect('/customer/list/')
