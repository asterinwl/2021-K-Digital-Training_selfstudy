class Dog:             #보통 클래스 이름은 대문자로 만들어준다.
    def __init__(self,name,breed,age,color):
        self.name=name
        self.breed=breed
        self.age=age
        self.color=color
    def eat(self):     #보통 필드 이름은 소문자로 만든다.
        print("%s가 음식을 먹는다." % self.name)
    def sleep(self):
        print("%s가 잠들었다." %self.name)
    def play(self):
        print("%s가 놀고 있다." %self.name)
    def __str__(self):
        return  "이름 : %s, 나이 : %d살, 품종 : %s" % (self.name, self.age, self.breed)
    def __lt__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.age ==other.age



dog1=Dog('바둑이','Nepolitan Mastiff',5,'Black')   #보통 객체 이름은 소문자로 만든다.
dog2=Dog('흰둥이','Maltese',2,'White')
dog3=Dog('초코','Chow Chow',3,"Brown")
dog1.eat()
dog2.eat()
dog3.eat()
dog1.sleep()
dog2.sleep()
dog3.sleep()
dog1.play()
dog2.play()
dog3.play()
print(dog1)
print(dog2)
print(dog3)
print(dog1<dog2)
print(dog1==dog2)
