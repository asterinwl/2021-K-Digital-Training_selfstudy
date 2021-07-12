''' 기존의 공식
def sootja():
    e=[]
    while 1:
        n= int((input('숫자를 입력하세요.(엔터키 누르면 종료) : ')))
        if n=='':   #엔터키 누르면 종료하게 하는것
           break
        else:
           e.append(n)
    return e
def pickup_even():
    e = sootja()
    f=[]
    for i in e:
        if i % 2==0 :
            f.append(i)
        else:
            continue
    return f

pickup_even()
'''

def sootja():
    e=[]
    while 1:
        n= input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n=='':   #엔터키 누르면 종료하게 하는것
           break
        else:
           e.append(n)
    return e

def pickup_even():
    e = sootja()
    f=[]
    for i in e:
        if int(i) % 2==0 :        #i에서 int(i)로 바꿈
            f.append(i)
        else:
            continue
    return f

print(pickup_even())              #print를 붙임

