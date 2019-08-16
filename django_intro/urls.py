"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# django_intro/urls.py
from django.urls import path
from pages import views #pages는 ../pages로 해야하지 않는가? 해도되는데 장고는 바로 어플리케이션 이름으로 해도된다.(스타일가이드~)

#장고의 목차를 생성하는 곳.
#www.ssafy.com/admin/ => 성공
#www.ssafy.com/login/ => '로그인 페이지 관련 함수'로 이동해!
urlpatterns = [
    # path('login/', 로그인 페이지 관련 함수)
    #path('사용자가 접속하는 경로')
    path('template_language/', views.template_language),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('greeting/<str:name>/', views.greeting),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('index/', views.index), #index() 가 아닌이유=> ()는 함수의 리턴값을 가져오고, 이거는 함수 그 자체를 가져옴
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('admin/', admin.site.urls),
]
