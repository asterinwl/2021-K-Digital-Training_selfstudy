#현금이 5000원이 있고 사탕 가격이 120원인 경우
#최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

m=5000
c=120
a=m//c
b=m%c
print('최대한 살 수 있는 사탕의 개수는 %d개이고 나머지 돈은 %d원이다.' % (a,b)) # % 앞에는 ,가 없다. 꼭 주의하자.

cash = 5000
candy = 120

A = cash // candy
B = cash % candy

print('사탕의 개수 : {0}개, 나머지 돈 : {1}원'.format(A, B)) #,가 아니라 . 이다.

print('잔액 : ' , format(125000.122,',.1f'))