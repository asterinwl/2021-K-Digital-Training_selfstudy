#클래스 상속 실습
#슈퍼클래스:사람 클래스   Person <- 서브클래스: 학생클래스 Studeent

class Person:
    def __init__(self,age,sex,name):
        self.age=age
        self.name=name
        self.sex=sex

    def greeting(self):
        print('안녕하세요')

class Student(Person):
    # 학교, 학과, 학번, 공부하다(), 시험보다()
    def __init__(self,age,sex,name,uni,major,stunum,study,test):
        super().__init__(age,sex,name)
        self.uni=uni
        self.major=major
        self.stunum=stunum
        self.study=study
        self.test=test

    def studentInfo(self):
        print("나이:%d 성별:%s 이름:%s 학교:%s 학과:%s 학번:%d" %(self.age,self.sex,self.name,self.uni ,self.major,self.stunum))
        print("%s을 공부하고 %s을 시험볼 예정입니다." %(self.study,self.test))

student1=Student(25,'F','가나다','한국대학교','컴퓨터공학과',20201574,'코딩','파이썬')
print(student1.studentInfo())
