from django.shortcuts import render,redirect
from students.models import Student    # Student 테이블 연결

# 학생정보수정페이지 열기
def update(request,no):
    qs = Student.objects.get(no=no)     # set타입 1개
    context = {'stu':qs}
    # qs = Student.objects.filter(no=no)  # 데이터 타입 - 리스트타입
    # context = {'stu':qs[0]}
    return render(request,'students/update.html',context)

def updateOk(request):
    return redirect('/students/list/')

# 학생정보 상세보기
def view(request,no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None    
    print('전달 no :',no)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보저장
def writeOk(request):
    # 학생정보저장
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    # 취미 - 리스트
    hobby = request.POST.getlist('hobby')
    # 리스트타입 -> str타입으로 변경
    hobby = ','.join(hobby)  # 'game,golf,swim'
        
    print("저장정보 이름 : ",name)
    print("저장정보 학과 : ",major)
    print("저장정보 hobby : ",hobby)  # ['game','golf','swim']
    
    Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo='등록합니다.').save()
    
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
