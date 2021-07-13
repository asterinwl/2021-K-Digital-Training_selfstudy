#함수의 매개변수 형식
#매개함수에 기본값 지정 :default parameter

def showMessage(message):
    print(message)

def showMessage2(name,message='Hello!'):
    print(name, message)

showMessage('Hello')
showMessage('Hi')
showMessage('We are happy!')
showMessage2('Kim','Hi')
showMessage2('Kim')

# def showMessage3(message='Hello!',name):
#     print(name, message)
# showMessage2()
# 오류가 발생한다. default argument(message='Hello!)는 맨 뒤에 써야 된다.

def showInfo(name,age=10,sex='F'):
    print(name,age,sex)

showInfo('홍길동')
showInfo('강감찬',40)
showInfo('변학도',40,'M')

#함수의 실인수로 리스트가 전달
def showNames(names):
    for name in names:
        print(name,end=" ")
names=['Hong','Park','Choi','Lee']
showNames(names)
print(" ")

#함수의 실인수로 딕셔너리가 전달
def showInfoStd(student):
    print(student)
    print('이름 : ', student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student.get('phone'))

inf_std={'name':'Kim','age':19,'phone':'010-1111-1023'}
showInfoStd(inf_std)

# 가변길이 매개변수
# *args : arguments 1개이상 지정
# **kwarge : keyword arguments key=value

def mySum(*args):
    total=0
    for x in args:
        total += x
    return total

print(mySum(1,3,5))
print(mySum(3,4))
print(mySum(1,2,4,5,6))
#print(mySum([1,2,4,5,6]))

def myShowInfo(**kwargs):
    for key in kwargs.keys() :
        print(key, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    for item in kwargs.items():
        print(item)

myShowInfo(id=123,name='Kim',address='Seoul')
myShowInfo(id=333,name='Lee')
myShowInfo(id=121,name='Hong',address='Daegu',phone='111-1111')

def calculator(operator, *args):
    pass

def studentInfo(name,age,sex):
    student = {'name':name,
               'age':age,
               'sex':sex
               }
    return student
print(studentInfo('Lee',30,'F'))
print(studentInfo(name='Kim',age=30,sex="M"))
print(studentInfo(name='Kim',sex="F",age=51))
#print(studentInfo(name='ho',15,'F')    오류가 뜬다.
#위치인수와 키워드인수를 혼용할때는 키워드인수는 위치인수 뒤쪽으로


