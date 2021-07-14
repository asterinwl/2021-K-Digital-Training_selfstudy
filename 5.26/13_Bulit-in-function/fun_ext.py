#재귀함수
'''
def selfCall():
    print('ha', end='')
    selfCall()
selfCall()                 #ha 계속 생기고 오류생김
'''
def selfcall(num):
    if num==0:
        return
    else:
        print('ha', end="")
        selfcall(num-1)

selfcall(5)
print('')

#팩토리얼 계산

def fact(num) :
    if num==1:
        return 1
    else :
        return num*fact(num-1)

print(fact(5))
#자연수를 입력받으면 해당하는 자연수까지 출력
#49 입력하면 1~49 출력

def count(num):
    a=[]
    for i in range(1,num+1):
            a.append(i)
    return a

print(count(5))

#내부함수 : 함수 내에서 정의된 함수

def outFunc(x,y):
    def inFunc(a,b):
        return  a+b
    return inFunc(x,y)
print(outFunc(10,20))
#print(inFunc(10,20))  #함수 안에서 지정되어있는 함수이므로 오류가 생긴다.

#
def hap(x,y):
    return x+y

print(hap(10,50))

print((lambda x,y : x+y)(10,50))

hap2=lambda x,y : x+y
print(hap2(10,20))

def hap(x=10,y=20):
    return x+y
print(hap())
print(hap(30,100))

hap3=lambda x=10, y=20 : x+y
print(hap3())
print(hap3(9,10))

#print((lambda x : y=10 ,x+y)(10)) 오류 발생
#람다함수 안에서 변수를 생성할 수 없다.

y=10
print((lambda  x:x+y)(1))

#람다함수 list 사용
for i in [1,2,3] :
    print(i)

lambda x:print(x)

#리스트의 값에 각각 10을 더하는 람다함수를 작성

#10을 더하는 함수
def addTen(x):
    return x + 10

print(list(map(addTen,[1,3,4])))

print(list(map(lambda x:x+10,[1,3,4])))

#2)lambda 표현식 정의

list1=[1,2,3,4]
list2=[10,20,30,40]

def addList(x,y):
    a=[]
    for i in range(4):
        a.append(int(x[i])+int(y[i]))
    return a
print(addList(list1,list2))

def hap(a, b):
    return [x + y for x, y in zip(a, b)]


print(hap(list1, list2))


print(list(map(lambda x,y:x+y,list1,list2)))

#print([(lambda x: x[0]+i[1])(i) for i in zip(list1,list2)])