#함수내에 사용되는 변수 : local variable(지역변수)

def show():
    a="Hello"     #지역변수:함수 내부에서만 사용 가능
    print(a)

a='Hi'            #전역변수
show()
print(a)

def show1(a):
    a=a+'Hello'
    print(a)

show1(a)
print(a)
show1('Haha')
print(a)        #a="Hi"를 각주시켰을때 a는 정의되지 않았다는 오류값이 뜬다.

def show2():
    print(a)          #함수 내에 a가 없으므로 a는 전역변수로 들어감.

a="Nice to meet you"  #a에 전역변수가 들어감. 즉 전역변수는 모든 곳에 사용가능한 것임.

show2()

# def show3():          #함수 내에 a가 있으므로 a는 지역변수로 들어감.
#     a=a+'H'           #따라서 a가 지정되어야 함.
#     print(a)
# show3()

#전역변수를 함수 내부세어 수정(변경)
def show3():
    global  a           #이때는 a는 지역변수가 아니라 전역변수로 지정된다.
    a=a+'H'
    print(a)
show3()

#실습문제
def sub(x,y):
    a = 7
    x,y = y,x
    b = 3
    print(a, b, x, y)
a, b, x, y =1, 2, 3, 4
sub(x,y)
print(a, b, x, y)

def sub(x,y):
    global a
    a = 7
    x,y = y,x
    b = 3
    print(a, b, x, y)
    print(id(a))
    print(id(x))
a, b, x, y =1, 2, 3, 4
print(id(a))
print(id(x))
sub(x,y)
print(a, b, x, y)

def showlist(mylist):
    mylist[0]=100
    print(mylist)

mylist=[1,2,3,4]
print(mylist)
showlist(mylist)
print(mylist)

def showlist(mylist):
    mylist[0]=100
    print(mylist)
    print('in function ID :',id(mylist))

mylist=[1,2,3,4]
print(mylist)
showlist(mylist)
print(mylist)
print('out function ID :',id(mylist))

#딕셔너리list를 dictionary로 변환
def getProduct(prdlist):
    name = prdlist['name']
    price = prdlist['price']
    return {'name':name,'price':price}

productL=[{'name':'notebook','price':1200000,'Maker':'삼성'},
          {'name':'smartPhone','price':1270000,'Maker':'삼성'},
          {'name':'냉장고','price':8700000,'Maker':'LG'},
          {'name':'에어콘','price':9740000,'Maker':'삼성'}]
for prdoct in productL:
    prdInfo=getProduct(prdoct)
    print(prdInfo)