from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('template_language/', views.template_language),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('search/', views.search),
    path('result/', views.result),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('greeting/<str:name>/', views.greeting),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('index/', views.index), #index() 가 아닌이유=> ()는 함수의 리턴값을 가져오고, 이거는 함수 그 자체를 가져옴
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
]