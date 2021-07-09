#정수 3개를 입력받아서 제일 큰 수를 출력

a =int(input('정수1 입력:'))
b =int(input('정수1 입력:'))
c =int(input('정수1 입력:'))

if (a>b and a>c) :
    max_num = a
elif (b>c) :  # elif (b>c)만 표현해도 괜찮다. 왜냐하면 이미 b>a를 내포해 있기 때문이다.
    max_num = b
else :
    max_num = c

print('제일 큰 수 : {}'.format(max_num))