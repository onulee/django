from django.shortcuts import render

# 차트페이지 호출
def chlist(request):
    profit = [20, 15, 7, 25, 27, 30]
    context = {'profit':profit}
    print("영업이익 : ",profit)
    return render(request,'chart/chlist.html',context)
