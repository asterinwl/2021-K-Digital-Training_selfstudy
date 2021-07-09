#컴퓨터와 게임하는 경우
from random import randint #randint에서 랜덤하게 뽑을 거야.
compNum=randint(1,100) #1과 100 사이에 아무식이나 적기
myNum=randint(1,100)
print('com : %d vs my: %d'%(compNum,myNum))
if(myNum>compNum):
    print('성공')
else:
    print('실패')

n=randint(1,100)
print(n)