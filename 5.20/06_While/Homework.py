for i in range(5) :
    for j in range(i,5) :
        print("*",end='')
    print()

n='*'
for i in range(1,6) :
    for j in range(5-i) :
        print (end="")
    for j in range(1,2*i) :
        print(n,end='')
    for j in range(i,5) :
        print(end='')
    print()

a=int(input('숫자 입력 : '))
while True:
    if a!=7 :
        a=int(input('다시 입력 : '))
    else :
        print('7 입력! 종료')
        break

a=int(input('숫자 입력 : '))
while True:
    if a==7 :
        print('7 입력! 종료')
        break
    else :
        a = int(input('다시 입력 : '))

money=10000
n=0
while True:
    if money>=2000 :
        n=n+1
        money=money-2000
        print("노래를 %d곡 불렀습니다." %n)
        print("현재 %d원 남았습니다." %money)
    else :
        if money==0 :
            print('잔액이 없습니다. 종료합니다.')
            break