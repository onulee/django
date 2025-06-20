from django.shortcuts import render

# 게시판리스트
def list(request):
    return render(request,'customer/list.html')
