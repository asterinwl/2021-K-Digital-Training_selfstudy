#클래스 상속(inheritance)
class Car(object):                #object는 최상위값이며 생략이 가능하다.
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

class Truck(Car):
    def __int__(self,speed,color,load):
        super().__init__(speed,color)   #부모 객체 사용
        self.load=load                 #필드 추가

    #매소드를 재정의 : 오버라이딩(overriding)
    def showLoad(self):
        print(self.load)

    def upload(self,up):
        self.load += up

    def showInfo(self):
        print('속도는 %d이고 적재량은 %d입니다.'%(self.speed,self.load))

car1=Car()
# car2=Truck(0,'Bule',10000)

car1.showInfo()
# car2.showInfo()
# car2.showLoad()
# car2.upSpeed(10)
# car2.showInfo()

#print(isinstance(car2,Car))
print(issubclass(Truck,Car))

class SportCar(Car):
    def __init__(self,speed,color,seats):
        super().__init__(speed,color)
        self.seats=seats

    def showInfo(self):
        print('Sport Car : 색상은 %s, 좌석수는 %d' %(self.color,self.seats))

car3=SportCar(0,'Red',2)
car3.showInfo()

# 다형성(polymorphism) : 동일한 이름의 매소드이지만, 다른 기능을 수행
carL=[car1,car3]

for car in carL:
    car.showInfo()
