#함수의 변환값(return)

def sum() :
    a=int(input('숫자1 입력 :'))
    b=int(input('숫자2 입력 :'))
    #print(a+b)
    return a+b   #반환을 해야지 정답을 가진다.
    #sum=a+b
    #return sum
# print(sum())
res=sum()
print('합은 %d' %res)

#삼각형의 넓이 계산 함수 get_triangle_area()
#높이와 밑변을 키보드로 입력
#결과값을 변환
#높이 :
#밑변 :
#삼각형의 면적 :

def get_triangle_area() :
    a=int(input('높이 : '))
    b=int(input('밑변 : '))
    area=a*b*(1/2)
    print('삼각형의 면적 : %.1f' % area)
    return area
get_triangle_area()

def get_triangle_area() :
    a=int(input('높이 : '))
    b=int(input('밑변 : '))
    area=a*b*(1/2)
    return area
area=get_triangle_area()
print('삼각형의 면적 : %.1f' % area)

#변환값이 여러 개인 경우
#변환값의 형식은 튜플
def get_triangle_area() :
    a=int(input('높이 : '))
    b=int(input('밑변 : '))
    area=a*b*(1/2)
    return a, b, area
area=get_triangle_area()
print('높이 %d, 밑변 %d, 삼각형의 넓이 %.1f' %(area[0], area[1], area[2]))

#첫 번째 값인 1이 나온다. return 후에는 입력이 완료되고 완전히 끝난다.
def multiReturn() :
    return 1
    return 2
    return 3
print(multiReturn())


def order() :
    a=int(input("상품가격 입력 : "))
    b=int(input("주문수량 입력 : "))
    print('-------------------------')
    return a, b, a*b
c=order()
print('상품가격 : %d원' %c[0])
print('주문수량 : %d개' %c[1])
print('주문액 : %d원' %c[2])

def order() :
    a = int(input("상품가격 입력 : "))
    b = int(input("주문수량 입력 : "))
    print("상품가격 : %d원"%a)
    print("주문수량 : %d개" % b)
    print("주문액 : %d원" %(a*b))

order()

#리스트 변환값
def getNames():
    names=[]
    for i in range(3):
        name=input('이름 입력 : ')
        nemes.append(name)

    return nemes
nameL=getNames()
print(type(nameL))
print(nameL)

#이름과 나이를 입력받아서 딕셔너리 형식으로 변환
#{'name':'홍길동','age':20}
def name_age():
    name_ages={}
    name=input('이름 입력 :')
    age=input('나이 입력 :')
    name_ages['name']=name
    name_ages['age']=age
    return name_ages
Name_age=name_age()
print(Name_age)

def name_age():
    name_ages={}
    name=input('이름 입력 :')
    age=input('나이 입력 :')
    name_ages={'name' : name , 'age' : age}
    return name_ages
Name_age=name_age()
print(Name_age)

def getInfo():
    info = dict()
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    info['name'] = name
    info['age'] = age

    return info

info = getInfo()
print(info)

for key, value in info.items():
    print(key,':',value)
for key in info.keys():
    print(key,":",info[key])


#변환값이 없는 경우 None 출력

def showHello():
    print('Hello')
result=showHello()
print(result)