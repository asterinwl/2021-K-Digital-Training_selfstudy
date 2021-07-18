#인스턴스 변수와 클래스 변수

class Car:
    number =0
    def __init__(self,speed=0,color='white'):
        self.color=color
        self.speed=speed
        Car.number += 1            #self를 쓰면 안되고 class의 이름을 써야한다.


    def __str__(self):
        return "안녕하슈"

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

# car1=Car()
# print(car1.getColor())
# car1.setColor('Red')
# print(car1.getColor())
# car1.showInfo()
# car1.upSpeed(20)
# car1.drive()
# car1.upSpeed(10)
# car1.drive()
# print("")

car1=Car()
#인스턴스 변수(필드)
print(car1.speed)
print(car1.color)
print(car1.number)

#클래스 변수
print(Car.number)

car2=Car(10,'Bule')
print(car2.speed)
print(car2.color)
print(car2.number)
print(Car.number)