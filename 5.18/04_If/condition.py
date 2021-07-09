#키보드로 입력받은 정수가 짝수인지 홀수인지 알 수 있는가?
num=int(input("숫자를 입력하세요")) #int를 이용해서 숫자인것을 반드시 나타내주어야 한다.
if (num%2==0) :     # :을 꼭 사용해야 된다. =은 값을 부여해주는 것이고 ==은 같음 여부를 나타내는 것이다.
    print('짝수')
else:
    print('홀수')    # 코드를 주지 않을 때는 pass 를 사용해도 된다. else를 쓴 다음 아무것도 안쓰면 오류. else를 안써도 같다.

#로그인 성공 코드 작성
ID=str(input('등록된 ID를 입력하세요.'))
password=int(input('비밀번호를 입력하세요.'))
if (ID=='flower' and password==1234) :
    print('로그인 성공!')
else:
    print('로그인 실패!')

ID = 'flower'
PW = '1234'

id = input('아이디 입력 : ')
pw = input('비밀번호 입력 : ')

if (id == ID and pw == PW):   #if 여러개라면 if->elif->else 순으로 간다.
    print('로그인 성공!')
else:
    print('로그인 실패!')


#1~10까지의 정수 합계 계산
