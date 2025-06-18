from django.shortcuts import render

# 공공데이터 리스트
def list(request):
    return render(request,'pboard2/list.html')
