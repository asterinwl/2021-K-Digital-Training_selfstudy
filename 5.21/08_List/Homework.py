
a=[]
while True:
    if len(a)!=3 :
        a.append(input("회원 입력 : "))
    else :
        print("회원 명단 : %s" %a )  #이런 식으로 나타내면 a의 형태가 list형으로 나타난다.
        print("회원 명단 : " , *a)   #이런 식으로 나타내면 a의 형태가 list형으로 나타나지 않는다.
        break


a=int(input("학생 수 입력 : "))
sum=over=0
for i in range(1,a+1) :
   b=input("학생%d 수 입력 : " %i)
   sum+=int(b)
   if int(b)>=80 :
      over+=1
print('총점 : %d' %sum)
print('평균 : %.2f' %(sum/a))
print('80점 이상 학생 : %d명' %over)

a=[]
while True:
        b = input("상품 등록 (엔터키 누르면 종료) : ")
        if b=='':
            break
        else :
            a.append(b)
print("등록된 상품 : " ,a)  #이런 식으로 나타내면 a의 형태가 list형으로 나타난다.
print("등록된 상품 : " ,*a) #이런 식으로 나타내면 a의 형태가 list형으로 나타나지 않는다.


