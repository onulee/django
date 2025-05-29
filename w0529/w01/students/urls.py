from django.urls import path,include
from . import views

# app_name는 / 붙이지 않음
app_name = 'students'
urlpatterns = [
    # path / 붙임.
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('writeOk/', views.writeOk, name='writeOk'),
    # html -> server 1.파라미터 2.api방식 3.js   <str:name>
    path('view/<int:no>/', views.view, name='view'),
    path('update/<int:no>/', views.update, name='update'), #학생정보수정페이지 열기
    path('updateOk/', views.updateOk, name='updateOk'), # 학생정보수정완료
]
