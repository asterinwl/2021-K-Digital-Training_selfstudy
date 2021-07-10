#문자열의 구성요소 판단
#isalpha() : 문자여부 True False

text='123457num'
print(text.isdigit())
print(text.isspace())
print(text.isalnum())
print(text.islower())
print(text.isupper())
print('----------------------')

print('a'.isdigit())
print('a '.isspace())
print('a'.isalnum())
print('a'.islower())
print('A'.isupper())
print('----------------------')

#연습문제. 문장을 입력하여 알파벳과 숫자,스페이스,그외 문자의 개수를 계산 출력
alphas=digits=space=others=0
string=input('문장을 입력하세요 : ')
for c in string:
    if c.isalpha():
        alphas +=1
    elif c.isdigit():
        digits +=1
    elif c.isspace():
        space +=1
    else :
        others +=1
print('문자 : %d개' %alphas)
print('숫자 : %d개' %digits)
print('공백 : %d개' %space)
print('그외 : %d개' %others)

