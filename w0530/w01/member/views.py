from django.shortcuts import render,redirect
from member.models import Member
from django.utils import timezone

### 로그인 - 페이지 : GET, 로그인 - 확인 : POST
def login(request):
    if request.method == 'GET': # 로그인페이지
        print("쿠키 : ",request.COOKIES)
        cook_id = request.COOKIES.get("cook_id") 
        # 찾는 데이터가 있으면 값, 없으면 빈공백으로 리턴
        c_info = request.COOKIES
        context = {"c_info":c_info,"cook_id":cook_id} # 쿠키모든 정보보기
        response = render(request,'member/login.html',context)
        if not request.COOKIES.get('cookieschk'):
            response.set_cookie("cookieschk",timezone.now())
        return response
        # return render(request,'member/login.html')
    elif request.method == 'POST': #로그인확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cook_id = request.POST.get('cook_id')
        print("아이디, 패스워드 : ",id, pw)
        

        # id,pw가 있는지 확인
        try:
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id  # session할당
                txt = 1
            else:
                txt = -1
        except:
            txt = 0
        
        # try:
        #     qs = Member.objects.get(id=id,pw=pw)
        #     request.session['session_id'] = id  # session할당
        #     txt = 1 # 성공
        # except:
        #     txt = 0 # 실패
        context = {'msg':txt}
        response = render(request,'member/login.html',context)
        if cook_id is not None:
            response.set_cookie('cook_id', id,max_age=60*60*24)
        else:
            response.delete_cookie("cook_id")    
        
        return response
        # return redirect('/')
        
def logout(request):
    request.session.clear() # 섹션모두삭제, del request.session['session_id']
    context = {'msg':2}
    return render(request,'member/login.html',context)        
