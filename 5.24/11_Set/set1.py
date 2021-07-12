
#set
#집합 만들기
s1={1,2,3,4,5}
print(s1)
print(type(s1))

#set() 함수로 집합 만들기
#리스트로 집합 생성
s2=set([10,20,30])
print(s2)
print(type(s2))

#튜플로 집합 생성
s3=set((100,200,300))
print(s3)
print(type(s3))

#index 사용이 불가능하다.
#s1[0]인 경우 오류가 뜬다.

#데이터 추가 .add()
s2.add(90)
print(s2)

s1.add(-9)
print(s1)

#데이터 삭제 .remove() .discard
s1.remove(-9)
print(s1)
#s1.remove(8)   에러 메시지가 뜬다.
s1.discard(4)
print(s1)

s1.clear()      #요소 완전히 지워버리기
print(s1)

del s1
print(s1)


#집합 연산 : union,intersection,difference

s1={3,4,1,6}
s2={2,4,5,8,3}
print(s1.union(s2))
print(s1.intersection(s2)) #매소드 함수
print(s1.difference(s2))
print(s2.difference(s1))

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

#set의 comprehensions 기능
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(*a)