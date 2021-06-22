### django 

```python
cd C:\Users\admin\Desktop\데이터 공부 자료\day26
```

`C:\Users\admin\Desktop\데이터 공부 자료\day26` 위치로 들어가자.



```python
cd ..
```

맨 처음 위치로 돌아가자.



```python
conda remove --name django --all
```

django 이름으로 되어있는 모든 파일을 삭제하라.



```django
django-admin startproject mysite
```

장고 안에서 `mysite`라는 프로젝트 만들기

```django
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

해당 구문을 치면 코드가 나온다.



```django
py manage.py runserver
```

로켓이 나오는 개발 서버를 만든다.

```django
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

6월 21, 2021 - 15:50:53
Django version 3.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

해당 구문을 치면 이런 코드가 나온다.

`http://127.0.0.1:8000/` 으로 들어가면 로켓이 발사되는 장면이 나온다.

코드 중에

`You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.`

이런 오류구문이 생기는 데 이는 정상이다.

이는 현재 데이터베이스에 적용되지 않은 변경사항들(migrations)에 대한 경고들인데 이는 내가 컴퓨터에 설정한 게 없어서 생기는 구문이다. 나중에 설정하고 마이그레이트를 하면 없어지는 구문이며 로켓을 보왔다면 크게 신경 쓰지 않아도 되는 구문이다.



```
py manage.py startapp polls
```

투표를 하는 파일을 하나 만든다.

나머지 사항들은 `https://docs.djangoproject.com/ko/3.2/intro/tutorial01/`을 따라 진행한다.

과정 중에 `polls/urls.py`을 만드는 과정이 있다.

이 때 파일명 뒤에  `.py`를 꼭 붙여주어야 `.py`로 나타난다.

```django
py manage.py runserver
```

이 코드를 작성하면,

최종적으로 브라우저에서 `http://localhost:8000/polls/`를 입력하면 index 뷰에 정의한 《*Hello, world. You’re at the polls index.*》 가 보일 것이다.

만약 에러 페이지가 표시된다면, `http://localhost:8000/ `이 아니라 `http://localhost:8000/polls/`가 정확히 주소 창에 입력되었는지 확인해라.



```django
py manage.py migrate
```

이 코드를 통해 mysql과 연결한다.

`settings.py`에서 

DATABASES = {

  'default':{

​    'ENGINE':'django.db.backends.mysql',

​    'NAME':'tip',

​    'USER':'root',

​    'PASSWORD':'9421',

​    'HOST':'localhost',

​    'PORT':'3306',

   }

}

으로 바꾼다.

`py manage.py shell`을 써서 완성한다.

그러면 mysql에 tip안에 여러 table이 생길 것이다.



```django
py manage.py runserver
```

최종적으로 브라우저에서 `http://localhost:8000/admin/`를 입력하면 로그인 화면이 생긴다.

만약 에러 페이지가 표시된다면, `http://localhost:8000/ `이 아니라 `http://localhost:8000/admin/`가 정확히 주소 창에 입력되었는지 확인해라.



#### Django 관리자 설정하기

관리 사이트에 로그인 할 수 있는 사용자를 생성해 보자.

```django
py manage.py createsuperuser
```

하는 username 을 입력하고 엔터를 누르고

```dj
Username: admin
```

그런 다음 원하는 이메일 주소를 입력하고

```django
Email address: admin@example.com
```

마지막으로, 암호를 입력하자.암호를 두번 물어보게 되는데, 두번째 입력하는 암호를 올바로 입력했는지를 확인하기 위한 암호이다.

```django
Password: **********
Password (again): *********
Superuser created successfully.
```

암호의 경우 작성을 하여도 코드로 나오지 않고 글자 수도 보이지 않는다.

따라서 주의하자.

```django
py manage.py runserver
```

이제, 웹 브라우져를 열고 로컬 도메인의  `http://127.0.0.1:8000/admin/`으로 접근 가능하고 로그인 화면이 보인다.

User 들어가면, 다른 유저 아이디도 생성 가능하다.
