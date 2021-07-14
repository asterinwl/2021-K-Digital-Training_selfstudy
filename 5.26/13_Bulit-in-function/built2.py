#계산과 관련된 내장 함수

#abs() : 절대값 계산

print(abs(-10))
print(abs(100))

#min() : 최소값 계산

print(min(1,-10,3))
print(min([-9,10,-30,3]))

#max() : 최대값 계산

print(max(1,-10,3))
print(max([-9,10,-30,3]))

#pow() : x*y
print(pow(2,10))

#divmod(a,b) : 나머지와 몫 => 결과 (//,%)
print(divmod(9,2))

#sum() : 합계
print(sum([1,-10,3]))     #list형태만 3개이상의 값을 받아줌.

#round() : 반올림
print(round(9.87))
print(round(9.87,1))
print(round(-9.87,1))
print(round(9.874333,3))

#enumerate(iterable,start=0)
#시퀀스(리스트,튜플,문자열,range)를 인덱스값을 포함하는 enumerate 객체로 반환
enum=enumerate(['apple','banana','melon','strawberry','kiwi','watermelon'])
print(enum)
for i, item in enum :
    print(i+1, item)

seasons=['Spring','Summer','Fall','Winter']
enumSeason=list(enumerate(seasons, start=1))
print(enumSeason)

#eval()
print(eval('3.1'))
print(eval('10+100'))

#filter(function,iterable) : 반복가능한 자료형 요소에 함수를 적용하여
#반환값이 참(True)인 결과만 걸러내어 반환

def positive(x) :
    return x>0

print(positive(9))
print(positive(-9))

result=filter(positive,[-10,0,3,-8,7])
print(type(result))
print(list(result))                    #값을 불러올때는 무조건 list를 사용한다.

#실습문제 : 짝수인지를 판별하는 함수 even(x)를 정의하고,
#이 함수를 filter를 이용하여 주어진 리스트의 짝수만 걸러내는 코드

def even(x) :
    return x%2==0

ans=filter(even,[-10,0,3,-8,7])
print(list(ans))

#질문
enum = enumerate(['apple', 'banana', 'melon'])

for e in enum:
    print(e)

print(enum)
print(list(enum))   #왜 list가 비었을까? -> enumerate를 객체 주소로 받는 경우
print('-'*30)       # __next()__나 __iter__()를 통해서 구성요소를 참조할때마다
                    #삭제 된다고 합니다 그래서 각각 1회 참조할수있다고 합니다.
                    #for문은 next문을 사용합니다.
#해결방법
enum = enumerate(['apple', 'banana', 'melon'])

for e in enumerate(['apple', 'banana', 'melon']) :
    print(e)

print(enum)
print(list(enum))

#next이면 과연 삭제될까?
f=iter(['a','b','c'])
print(next(f))
print(next(f))
print(next(f))

print(list(f))         #삭제된다.

#list()
print(list("sunflower"))   #각각의 값이 분리되어 나온다.

#sorted(iterable, key=Nome, reverse=False
print(sorted([10,-4,5]))
print(sorted([10,-4,5], reverse=True))
print(sorted("flower"))
print(sorted("flower",key=str.lower))

#range
print(type(range(5)))
print(list(range(5)))
print(list(range(2,10,3)))
print(tuple(range(5)))

#zip(*literable) : 각 iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(zip([1,3,5],['cat','dog','hourse']))
print(list(zip([1,3,5],['cat','dog','hourse'])))
print(list(zip([1,3,5],['cat','dog','hourse','lion'])))
print(tuple(zip([1,3,5],['cat','dog','hourse'])))

keys=['cat','dog','hourse']
values=[1,3,5]
result=dict(zip(keys,values))
print(result)

#map
result=list(map(str,range(10)))  #꼭 list형으로 만들어주어야 값이 나옴.
print(result)
print(list(map(int,result)))