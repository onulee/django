from django.shortcuts import render,redirect
from students.models import Student    # Student 테이블 연결

# 학생정보 상세보기
def view(request,no):
    Student.objects.get(no=no)
    print('전달 no :',no)
    return render(request,'students/view.html')

# 학생정보저장
def writeOk(request):
    # 학생정보저장
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
        
    print("저장정보 이름 : ",name)
    print("저장정보 학과 : ",major)
    
    Student(name=name,major=major,grade=grade,age=age,gender=gender,memo='등록합니다.').save()
    
    return redirect('/students/list/')

# 학생정보등록페이지 열기
def write(request):
    return render(request,'students/write.html')

# 학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    # render 폴더앞에 / 안붙임.
    return render(request,'students/list.html',context)
