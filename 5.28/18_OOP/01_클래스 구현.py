#클래스 구현:메서드,필드 정의, 생성자 이용

#클래스 선언
#class 클래스 이름[(슈퍼클래스명)] :
class Car:
    pass

car1=Car()
print(car1)
#<__main__.Car object at 0x00000157CDDBE250>

class Car:
    #메소드 정의
    def show(self):
        print('시험중입니다')

#인스턴스 생성
car1=Car()
car2=Car()
car3=Car()
print("------")
#매소드 호출
car1.show()
car2.show()
car3.show()

#특정 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)

print(isinstance(car1,Car))
print(isinstance(car1,int))

x=3
print(isinstance(x,int))

y=list([1,2,3,4])
print(isinstance(y,list))

print(type(x))

z="HI,반가워요"
print(type(z))

a=True
print(type(a))

#파이썬에서 기본제공하고 있는 int,float,bool,str,list,dict,set,tuple
#=>클라스

print(isinstance(a,int))   #참,거짓 값은 사실 상수값이다. 1=True 0=False

b=(1,2,3)
print(type(b))
print(isinstance(b,list))

#instance&object
#같은 것 가리키고 있음
#instance:클래스와 연관지어 말할 때
#예.car1은 Car 클래스의 인스턴스이다.
#object:단독으로 부를 때
#예.car1 객체

print('---------------------필드 추가---------------------')
#필드 추가 : 메소드 내에서 사용

class Car:
    def show(self):
        print('시험중입니다')
    def drive(self):
        self.speed=60   #speed 필드
        print(('%d로 주행중입니다' %self.speed))

#메인 : 인스턴스를 생성하고 이용
car1=Car()
car1.drive()
print(car1.speed)
car1.speed=100
car1.drive()             #값이 바뀌지 않는다.
print(" ")

class Car:
    def show(self):
        print('시험중입니다')
    def drive(self,speed):
        self.speed = speed  #speed 필드
        print(('%d로 주행중입니다' %self.speed))

#메인 : 인스턴스를 생성하고 이용
car1=Car()
car1.drive(70)
print(car1.speed)
car1.speed=100
car1.drive(50)             #값이 바뀐다.

#메인:인스턴스를 생성하고 이용
car1=Car()
car1.drive(70)
print(car1.speed)
car1.speed=100
car1.drive(50)
print("")

#인스턴스.필드
car1.color="red"
print(car1.color)

#클래스에서 필드 선언
class Car:
    speed=0
    color=''
    def show(self):
        print('시험중입니다')
    def drive(self):
        print(('%d로 주행중입니다' %self.speed))
mycar=Car()
print(mycar.speed)
mycar.drive()
mycar.speed=60
mycar.drive()
print('')

print('---------------------생성자---------------------')
#생성자(consrutor) : 인스턴스를 생성해주는 함수
#기본 생성자:인스턴스 호출 =>인스턴스명
class Car:
    def __init__(self):
        self.color='white'
        self.speed=0
    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.'%self.color)
    def drive(self):
        print(('%d로 주행중입니다' % self.speed))
mycar=Car()
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed=50
mycar.drive()
print(" ")

#매개변수가 있는 생성자 __int__(self, 매개변수1,매개변수2,....)
#=>필드 초기값 지정
class Car:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.'%self.color)
    def drive(self):
        print(('%d로 주행중입니다' % self.speed))

mycar=Car('red',200)
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed=50
mycar.drive()
print(" ")

yourcar=Car('blue',0)
yourcar.showInfo()
print(" ")

class Car:
    def __init__(self,speed=0,color='white'):
        self.color=color
        self.speed=speed
    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.'%self.color)
    def drive(self):
        if self.speed != 0 :
            print(("%d로 주행중입니다." %self.speed))
        else:
            print('정차중입니다.')

car1=Car()
car2=Car(color='yellow')
car3=Car(10,'bule')
car4=Car(10)
car5=Car(color='black',speed=50)
car1.showInfo()
car2.showInfo()
car3.showInfo()
car4.drive()
print(car5.speed)
print(car5.color)
print("")

class Car:
    def __init__(self,speed=0,color='white'):
        self.color=color
        self.speed=speed

#def __str__(self):

    #color 필드 값을 반한
    def getColor(self):
        return self.color

    #color 필드값 변경매소드
    def setColor(self,color):
        self.color=color

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.'%self.color)
    def drive(self):
        if self.speed != 0 :
            print(("%d로 주행중입니다." %self.speed))
        else:
            print('정차중입니다.')

    def upSpeed(self,up):
        self.speed += up
    def downSpeed(self,down):
        if self.speed > 0 :
            self.speed -= down
        else :
            self.speed=0

car1=Car()
print(car1.getColor())
car1.setColor('Red')
print(car1.getColor())
car1.showInfo()
car1.upSpeed(20)
car1.drive()
car1.upSpeed(10)
car1.drive()
print("")
#비공개 필드   __ 클래스 내에서만 사용하는 비공개 필드
# class Car:
#     def __init__(self,speed=0,color='white'):
#         self.__color=color
#         self.speed=speed

#비공개 매소드 __필드명
# color 필드 값을 반한
def getColor(self):
    return self.__color


# color 필드값 변경매소드
def setColor(self, color):
    self.__color = color


def __showInfo(self):
    print('이 자동차의 색상은 %s입니다.' % self.__color)


def drive(self):
    if self.speed != 0:
        print(("%d로 주행중입니다." % self.speed))
    else:
        print('정차중입니다.')

car1=Car()
print(car1.getColor())
car1.setColor('Red')
print(car1.getColor())
car1.showInfo()