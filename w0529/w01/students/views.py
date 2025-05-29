from django.shortcuts import render
from students.models import Student    # Student 테이블 연결

# 학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    
    # render 폴더앞에 / 안붙임.
    return render(request,'students/list.html',context)
