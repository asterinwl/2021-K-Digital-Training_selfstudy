for i in range(5):
    print('*', end= '')
print()
for i in range(4):
    print('*', end= '')
print()
for i in range(3):
    print('*', end= '')
print()
for i in range(2):
    print('*', end= '')
print()
for i in range(1):
    print('*', end= '')
print()

print("----------------")

for j in range(5,0,-1):
    for i in range(j):
        print("*",end='')
    print()

print("----------------")

for j in range(5,0,-1):
    for i in range(j):
        print(" ",end='')
    for i in range(j) :
        print("*")

for i in range (1,6) :
    print(' '*(6-i)+'*'*(2*i-1))
print("----------------")

money=10000
n=0
while True:
        n=n+1
        money=money-2000
        print("노래를 %d곡 불렀습니다." %n)
        if money==0 :
            print('잔액이 없습니다. 종료합니다.')
            break
        else :
            print("현재 %d원 남았습니다." % money)