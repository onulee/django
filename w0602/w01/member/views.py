from django.shortcuts import render,redirect

### login페이지연결, login확인
def login(request):
    if request.method == 'GET':
        # idCheck쿠키를 읽어와서 있으면, 저장된 아이디를 리턴해서 돌려줌.
        # 모든 쿠키 읽어오기 request.COOKIES
        print("모든 쿠키 : ",request.COOKIES)
        # 해당쿠키 읽어오기
        idCheck = request.COOKIES.get('idCheck','') # 없으면 ''빈공백 처리
        context = {'save_id':idCheck}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id') #아이디
        pw = request.POST.get('pw') #패스워드
        idCheck = request.POST.get('idCheck') # 있을수도 있고, 없을수도 있고
        print("아이디,패스워드 : ",id,pw)
        if idCheck != None:
            print('idCheck가 체크 되었습니다.')
            # 쿠키에 id를 저장해서 돌려줌.
            
        else:
            print('idCheck가 체크되지 않았습니다.')    
        
        return render(request,'member/login.html')
        # return redirect('/')
        
