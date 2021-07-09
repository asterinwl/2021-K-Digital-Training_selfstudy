# eval=문자열을 숫자열로 바꿔줌

num1=eval(input('number1 : '))
num2=eval(input('number2 : '))
print(type(num1))
print(type(num2))
total=num1+num2
print('합은 {}'.format(total))

print(eval(input())) #이 함수는 간단한 계산이 가능하며 7+8을 계산했다.


