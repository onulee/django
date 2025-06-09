from django.urls import path,include
from . import views

app_name = 'member'
urlpatterns = [
    path('step01/', views.step01, name='step01'),
    path('step02/', views.step02, name='step02'),
    path('step03/', views.step03, name='step03'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
