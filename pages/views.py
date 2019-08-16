# pages/views.py
from django.shortcuts import render
from datetime import datetime
import random


def index(request):      # 첫 번째 인자는 반드시 request=>사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html') #render의 첫번째 인자도 반드시 request가 들어간다.

def introduce(request):
    return render(request, 'introduce.html')
#Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name
    }

    #딕셔너리 형식으로 넘겨줘야함
    return render(request, 'dinner.html', context)

def image(request):
    image_url = 'https://picsum.photos/400/300'
    context = {
        'image_url': image_url,
    }

    return render(request,'image.html',context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'result': num1 * num2,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'times.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def isitbirthday(request):
    mybirthday = datetime(1993,6,16)
    context = {
        'mybirthday': mybirthday,
    }
    return render(request, 'isitbirthday.html', context)

def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = random.sample(list(range(1,46)),6)
    # lotto = [21, 25, 30, 32, 40, 42]
    lotto.sort()
    context = {
        'real_lotto': real_lotto,
        'lotto': lotto,
    }
    return render(request, 'lotto.html', context)

