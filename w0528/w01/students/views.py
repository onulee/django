from django.shortcuts import render

# 학생정보 등록
def write(request):
    return render(request,'students/write.html')

# 학생정보 리스트
def list(request):
    return render(request,'students/list.html')
