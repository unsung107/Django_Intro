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
from django.urls import path, include
#장고의 목차를 생성하는 곳.

#www.ssafy.com/admin/ => 성공
#www.ssafy.com/login/ => '로그인 페이지 관련 함수'로 이동해!
urlpatterns = [
    # path('login/', 로그인 페이지 관련 함수)
    #path('사용자가 접속하는 경로')
    path('pages/', include('pages.urls')),
    path('utilities/', include('utilities.urls')),

    path('admin/', admin.site.urls),
]
