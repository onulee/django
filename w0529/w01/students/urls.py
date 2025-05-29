from django.urls import path,include
from . import views

# app_name는 / 붙이지 않음
app_name = 'students'
urlpatterns = [
    # path / 붙임.
    path('list/', views.list, name='list'),
]
