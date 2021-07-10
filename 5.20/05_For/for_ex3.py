#두 숫자를 입력받아서 이 두 수 사이의 숫자의 합을 구하기
num1=int(input('숫자 하나를 입력하세요. : '))
num2=int(input('숫자 하나를 입력하세요. : '))
sum=num1                                             #이 항목 전에 sum=0을 할당해주는 것도 방법
for i in range(num1,num2+1) :
    sum += i
print('%d와 %d사이의 합은 %d' %(num1,num2,sum-num1))   #그러면 sum만 써도 되겠지??

#단 수를 입력받아서 해당 구구단 출력
num3=int(input('숫자 하나를 입력하세요. : '))
for a in range(1,10) :
    num4=num3*a
    print('%d * %d = %d ' %(num3,a,num4))

#카운트 다운 프로그램 작성
num5=int(input('시작 숫자를 입력하시오 : '))
for b in range(num5,0,-1) :
     print("%d " %b,end=' ')
print('발사')
