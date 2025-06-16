from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member

# id중복확인
def idchk(request):
    id = request.POST.get('id','')
    print('넘어온 id : ',id);
    ## DB확인 - Member테이블
    try:
        qs = Member.objects.get(id=id)
        print(qs)
        result = 1
    except:
        result = 0    
     
    print("확인 : ",result)       
    context = {'result':result}
    return JsonResponse(context)

def step04(request):
    return render(request,'member/step04.html')

def step03(request):
    return render(request,'member/step03.html')

def step02(request):
    return render(request,'member/step02.html')

def step01(request):
    return render(request,'member/step01.html')
