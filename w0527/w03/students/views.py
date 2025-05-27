from django.shortcuts import render

def view(request):
    # get방식
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 : ",name)
    print("나이 : ",age)
    context = {"name":name,"age":age}
    return render(request,'students/view.html',context)


def list(request):  
    # request -> id=aaa, pw=1111, gender='남자'
    id = request.POST.get("id")  # 변수
    pw = request.POST.get("pw")  # 변수
    gender = request.POST.get("gender") # 변수
    hobbys = request.POST.getlist("hobby") # 리스트
    print("입력된 id : ",id)
    print("입력된 pw : ",pw)
    print("입력된 gender : ",gender)
    print("입력된 hobbys : ",hobbys)
    context = {"id":id,"pw":pw,"gender":gender,"hobby":hobbys }
    return render(request,'students/list.html',context)
