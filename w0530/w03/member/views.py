from django.shortcuts import render
from member.models import Member  #Member테이블 호출

# 로그아웃 부분
def logout(request):
    # session 모두 삭제
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)


# 로그인 부분
def login(request):
    if request.method == 'GET':  # 로그인페이지 열기
        return render(request,'member/login.html')
    # 아이디저장 체크박스
    elif request.method == 'POST': # ID,PW확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        # 쿠키저장
        
        # id,pw확인 - 없을때 error발생 예외처리
        try:
            qs = Member.objects.get(id=id,pw=pw)
            ## session 추가
            request.session['session_id'] = qs.id
            request.session['session_nickName'] = qs.nickName
            msg = 1  # id,pw가 있음.
            print("데이터 여부 : 존재함")
        except:
            msg = 0  # id,pw가 없음.
            print("데이터 여부 : 없음")
        context = {"msg":msg}
        return render(request,'member/login.html',context)
        