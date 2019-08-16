# pages/views.py
from django.shortcuts import render
from datetime import datetime
import random
import requests
url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=870'

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

def search(request):
    return render(request, 'search.html')

def result(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category':category,
    }
    return render(request, 'result.html', context)

def lotto_result(request):
    lotto_numbers = request.GET.get('lotto_numbers')
    lotto_numbers = list(map(int,lotto_numbers.split()))
    lotto_numbers.sort()

    response = requests.get(url)
    lotto_info = response.json()
    bonus = lotto_info['bnusNo']
    print(lotto_info)

    goal = []
    for k in lotto_info.keys():
        if 'drwtNo' in k:
            goal.append(lotto_info[k])

    # goal = [21, 25, 30, 32, 40, 42]
    grade = {
        6: '1등',
        5: '3등',
        4: '4등',
        3: '5등',
    }
    print(lotto_numbers)
    count = 0
    for i in range(6):
        if lotto_numbers[i] in goal:
            count += 1
    if grade.get(count) != None:
        if count == 5 and bonus in lotto_numbers:
            result = '2등'
        else:
            result = grade[count]
    else:
        result = '꽝'

    context = {
        'lotto_numbers': lotto_numbers,
        'result': result,
        'goal': goal,
        'bonus': bonus,

    }
    
    return render(request, 'lotto_result.html', context)

def lotto_pick(request):
    return render(request, 'lotto_pick.html')

def static_example(request):
    return render(request, 'static_example.html')