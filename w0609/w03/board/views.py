from django.shortcuts import render

def view(request):
    return render(request,'board/view.html')

def list(request):
    return render(request,'board/list.html')
