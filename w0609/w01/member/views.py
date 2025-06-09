from django.shortcuts import render


# 회원가입부분
def step03(request):
    return render(request,'member/step03.html')

# 약관동의부분
def step02(request):
    return render(request,'member/step02.html')

# 이메일인증부분
def step01(request):
    return render(request,'member/step01.html')
