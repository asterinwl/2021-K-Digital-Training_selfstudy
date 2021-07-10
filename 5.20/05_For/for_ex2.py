#1에서 20까지의 정수 중 3의 배수 출력하고 합계 구하기
sum=0
for i in range(3,21,3) :   #3부터 시작해야 3의 배수가 된다. range(1,21,3)이 아니다.
    sum+=i
    print(i,end=' ')    #tap=뛰어써야 모든 것이 나옴.
print(sum)
print('\n--------------------')
#range()의 step 인수를 사용하지 않고 구하기

sum=0
for i in range(21) :
    if i % 3==0 :
        sum=sum+i #뛰어쓰기가 매우 중요하다. if다음의 공식은 뛰어쓰기를 열심히 해주어야 한다.
    print(i,end=' ')
print('\n')
print(sum)