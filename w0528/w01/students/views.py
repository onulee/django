from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

# 학생정보 등록
def write(request):
    if request.method == 'POST':  # POST방식으로 들어올때 - 정보를 DB저장
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보 : ",name,major,grade,age,gender)
        print("request method : ",request.method)
        return redirect('/')
        
    else: # GET방식으로 들어올때
        print("request : ",request)
        print("request get : ",request.GET)
        print("request method : ",request.method)
        return render(request,'students/write.html')

# 학생정보 리스트
def list(request):
    return render(request,'students/list.html')
