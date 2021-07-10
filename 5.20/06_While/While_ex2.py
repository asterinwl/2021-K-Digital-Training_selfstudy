x=0
while x<10 :
    x +=1
    if x%2==0 :     #짝수
        continue
    print(x,end='')

x=0
while x<10 :
    x +=1
    if x%2==0 :     #짝수
        break
    print('\n %d'%x)

while True:
    print("반복 수행되는 문장입니다")
    answer=input("종료 하려면 x 입력 : ")
    if answer=='x' :
        break
print('반복 종료')