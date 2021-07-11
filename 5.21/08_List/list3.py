#리스트 주요 메소드

#리스트의 길이 계산 함수 : len(리스트명)
a=[1,2,3,4,5,6,3,9,3]
print('리스트의 길이 : %d' %len(a))

#리스트의 요소
print(a.count(3))

#리스트의 요소 추가, 삽입 : append(), insert()
a.append(100)
print(a)

a.append([110,120])
print(a)

a.insert(2,120)             #3번째 위치에 120을 넣을 거다.
print(a)

b=[]
print(b)
b.append(5.5)
print(b)
b.append(10.5)
print(b)
b.append(6.5)
print(b)

scores=[]
for i in range(10):
    score = int(input('점수입력:'))
    #scores.append(score)
    scores.insert(0,score1)
print(scores)

#리스트의 요소를 제거 : remve(), pop()

#remove(삭제하려는 값) : 가장 첫 번째 만나는 값을 삭제
n=[1,2,3,4,5,3,4,-1,-5,10]
# n.remove(-1)
# print(n)
# cnt=n.count(3)
# print(cnt)
# print(cnt)

#pop() : 맨마지막 값은 삭제, pop(index) : index위치의 값을 삭제, 변환
data=n.pop()    #마지막 수에 해당됨.
print(n)
print(data)

data=n.pop(4)   #5번째 자리 수에 해당됨.
print(n)
print(data)