from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student  #Student테이블

# 학생정보 등록
def write(request):
    if request.method == 'POST':  # POST방식으로 들어올때 - 정보를 DB저장
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보 : ",name,major,grade,age,gender)
        ## DB저장
        ## 1. 데이터.save() / 2. create() 
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        return redirect('/students/list/')
        
    else: # GET방식으로 들어올때
        print("request method : ",request.method)
        return render(request,'students/write.html')

# 학생정보 리스트
def list(request):
    # DB검색 
    # objects.all():전체가져오기, objects.get(): 해당되는것가져오기
    # objects.filter(): 검색기능
    # objects.order_by() : 정렬, -정렬
    # qs = Student.objects.all() # 전체가져오기
    qs = Student.objects.order_by('-id') # 순차정렬
    context = {'list':qs,'count':100,'id':'aaa'} # 딕셔너리 타입으로 전달
    return render(request,'students/list.html',context)
