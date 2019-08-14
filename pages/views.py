# pages/views.py
from django.shortcuts import render
import random

def index(request):      # 첫 번째 인자는 반드시 request=>사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html') #render의 첫번째 인자도 반드시 request가 들어간다.

def introduce(request):
    return render(request, 'introduce.html')
#Template Variable Example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }
    
    #딕셔너리 형식으로 넘겨줘야함
    return render(request, 'dinner.html', context)

