scores=[90,57,88,45,78]
num=0
for score in scores :
    num=num+1
    if score >= 60 :
        result="합격"
    else :
        resule="불합격"
    print("%d번 %d점 %s" % (num,score,result))


#숫자 10개를 입력 받아서 양,음,0의 개수 출력하기
a=int(input("숫자1입력 : "))
b=int(input("숫자2입력 : "))
c=int(input("숫자3입력 : "))
d=int(input("숫자4입력 : "))
e=int(input("숫자5입력 : "))
f=int(input("숫자6입력 : "))
g=int(input("숫자7입력 : "))
h=int(input("숫자8입력 : "))
i=int(input("숫자9입력 : "))
j=int(input("숫자10입력 : "))

print(" -------------------")

A=[a,b,c,d,e,f,g,h,i,j]
k=l=m=0
for an in A :
    if an > 0 :
        k+=1
    elif an == 0  :
        l+=1
    else :
        m+=1
print("양의 개수 : %d " %k)
print("음의 개수 : %d " %m)
print("0의 개수 : %d " %l)

''' 이 방법이 더 고급스럽다.
positive = negative = zero = 0

for i in range(1,11):
    numb = int(input('숫자 %d 입력 : ' % i))
    if numb > 0:
        positive += 1
    elif 0 > numb:
        negative += 1
    else:
        zero += 1
print('--------------------')
print('양의 개수 : %d \n음의 개수 : %d \n 0의 개수 : %d' % (positive, negative, zero))
'''