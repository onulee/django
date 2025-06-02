from django.shortcuts import render

# 글쓰기
def write(request):
    return render(request,'board/write.html')

# 게시판리스트
def list(request):
    return render(request,'board/list.html')
