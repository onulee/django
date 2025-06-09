from django.shortcuts import render
from member.models import Member

# 로그아웃부분
def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)

# 로그인부분 - get, post
def login(request):
    if request.method == 'GET':
        ## 쿠키 읽어오기
        cook_id = request.COOKIES.get('cook_id','')
        context = {'cook_id':cook_id}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print("로그인 넘어온 데이터 : ",id,pw,idsave)
        ## id,pw확인
        msg = 0
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = id #session id를 추가
            msg = 1
        except: print('데이터가 없습니다.')    
        ## 쿠키 읽어오기
        cook_id = request.COOKIES.get('cook_id','')
        context = {'msg':msg,'cook_id':cook_id}
        response = render(request,'member/login.html',context)
        ## 쿠키저장
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24*30)
        else:
            response.delete_cookie('cook_id')    
        return response
        

# 회원가입부분
def step03(request):
    return render(request,'member/step03.html')

# 약관동의부분
def step02(request):
    return render(request,'member/step02.html')

# 이메일인증부분
def step01(request):
    return render(request,'member/step01.html')
