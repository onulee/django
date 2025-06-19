from django.shortcuts import render
from member.models import Member

# get:로그인페이지, post:로그인확인
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        return render(request,'member/login.html')
        

# 회원가입01
def step01(request):
    return render(request,'member/step01.html')
