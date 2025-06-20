from django.shortcuts import render

# 하단댓글리스트
def clist(request):
    context = {}
    return render(request,'customer/list.html',context)

