## Django Setting
### 가상환경

프로젝트 하나당 파이썬 환경 하나씩 둘것입니다.

왜그렇게 하느냐... 프로젝트마다 사용하는 라이브러리가 다 다를 수 있고 버젼이 다를 수 있다.

호환성, 의존성이 생김.

```bash
# 파이썬 버젼 확인
$ python -V
Python 3.7.4

# 가상환경 생성
# python -m venv <가상환경 설치경로>
$ python -m venv venv

# 가상환경 적용
$ source venv/Scripts/activate

# 버전확인
(venv) # <= 가상환경 적용 시 git bash에서 해당 환경 이름이 표시된다.
$ python -V
Python 3.7.4

# 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

# pip upgrade
(venv)
$ python -m pip install --upgrade pip

# pip upgrade 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```



---

## VS Code 및 기타 세팅

### VS Code 파이썬 환경 선택

- VS Code Extensions에서 `Python`과 `Django` 설치

- 'Ctrl + Shift + P' => `Python select interpreter` => 방금 생성한 가상환경을 선택(`.venv/Scripts/python.exe`)
  - `.vscode/settings.json` 파일이 생성되며 터미널에서 자동으로 가상환경이 적용된다면 OK



### Git ignore 세팅

- gitignore.io 에 접속하여 `python`, `django`, `windows`, `visual studio code` 선택 후 생성 및 복사
- `.gitignore` 파일 생성 후 붙여넣기



### VS Code Django 환경 세팅

```json
{
    //파이썬 환경선택 => 자동으로해줌
    "python.pythonPath": "venv\\Scripts\\python.exe",

    // Django 에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    // django-html 에서도 html emmet (! tab) 을 적용
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html 에서 tab size 를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    },
}

```



---

## Start Django project

```bash
(venv)
$ pip install django
```

- Django를 설치한 순간부터 `django-admin` 이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django project 에 여러가지 명령을 할 수 있다.

### Start project

```bash
(venv)
$ django-admin startproject django_intro .
```

- 현재 디렉토리에서 django_intro 라는 이름으로 프로젝트를 시작하겠다.

- Django project naming

  - \- 캐릭터는 사용 될 수 없다.

  - python과 django에서 이미 사용되는 이름은 사용하지 않는다.

    (django 라는 이름은 django 그 자체와 충돌이 발생하며, test라는 이름도 django 내부적으로 사용하는 모듈이름)

### Run server

```bash
$ python manage.py runserver
```

- Ctrl + c 커맨드로 종료한다.
- 기본적으로 `localhost:8000`에서 실행이 된다.



app

- models.py => 데이터베이스를 담당한다

- views.py => 로직들을 담당한다

- urls.py => 사용자가 들어올 수 있는 경로를 설정

APP을 만든 후에 프로젝트 폴더/ settings.py에서 출생신고를 해줘야함. (settings.py/ 33lines INSTALLED_APPS)