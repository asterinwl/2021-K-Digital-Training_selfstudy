a=input('16진수 한 글자 입력 : ')

if a=='A' or a=='a' :
    print('10진수 ==> {}'.format(10))
elif a == 'B' or a == 'b':
    print('10진수 ==> {}'.format(11))
elif a == 'C' or a == 'c':
    print('10진수 ==> {}'.format(12))
elif a == 'D' or a == 'd':
    print('10진수 ==> {}'.format(13))
elif a == 'E' or a == 'e':
    print('10진수 ==> {}'.format(14))
elif a == 'F' or a == 'f':
    print('10진수 ==> {}'.format(15))
else:
    print("16진수가 아닙니다.")

#'a'<= a <= 'f' 식으로 나타내도 좋다. 답 : 'a'<= a <= 'f' or 'A'<= a <= 'F' or '0'<= a <= '9'
#print(int('  ',16) 이 16진수로 바꾸는 것이다. 이미 위에 문자로 입력받았으므로 이 경우는 print(int(a,16)으로 나타내면 좋다.

money=int(input('교환할 돈 입력 : '))

a=money//50000
b=(money%50000)//10000
c=(money%10000)//5000
d=(money%5000)//1000
e=(money%1000)//500
f=(money%500)//100
g=(money%100)//50
h=(money%50)//10
i=money%10

print('50,000원 %d장, 10,000원 %d장, 5,000원 %d장, 1,000원 %d장,\n 500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개,' %(a,b,c,d,e,f,g,h))
print('바꾸지 못한 돈: %d 원' % i )

#print(end=--------------------------------------- \n) 을 이용해서 끝남을 표현할 수 있다.


from random import randint
A=randint(1,6)
B=randint(1,6)
print('A의 주사위 숫자는 %d 입니다.' %A)
print('B의 주사위 숫자는 %d 입니다.' %B)
if A>B :
    print('A가 이겼다.')
elif A==B :
    print('둘 다 비겼다.')
else :
    print('B가 이겼다.')

#import random
# a=random.randrange(1,7) 이런식으로도 계산 가능하다.