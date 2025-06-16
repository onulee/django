from django.shortcuts import render

# 차트페이지 호출
def chlist(request):
    return render(request,'chart/chlist.html')
