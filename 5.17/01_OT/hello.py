
'''
# 변수에 값을 저장
x = 10
y = 20
z = 30
print(x, y, z)
print(x)
print(y)
print(z)

# 여러개의 변수에 여러개의 값을 저장
x, y, z = 10, 20, 30
print(x, y, z)
print(x)
print(y)
print(z)

# 여러개의 변수에 동일한 값을 할당
a = b = c = 100
print(a, b, c)



#두 변수의 값을 교환(swap)
a,b=10,20
a=10
b=20
print("a=",a)
print("b=",b)

print('[swap]')

c=a
a=b
b=c

print("a=",a)
print("b=",b)

a,b=b,a

print("a=",a)
print("b=",b)


#변수를 삭제
x=100
print(x)
print(id(x))
print(type(x))

delx

print(x)

#문자열에 큰 따옴표 사용
name = "김민형"
age=26
print(name,age)

address='경기도 용인시 기흥구'
print(name+"은 "+address+"에 삽니다")

#str()은 형변환 함수이다.
#print(name+'은 '+age+'살 입니다')
print(name+'은 ',age,'살 입니다')
print(name+'은 '+str(age)+'살 입니다')


#사각형의 면적을 구하는 프로그램

width=100
height=50
area=width*height
print('사각형면적은',area)

name='홍길동'
no=2016001
year=4
grade='A'
average=93.5


print('성명 :',name)
print('학번 :',no)
print('학년 :',year)
print('학점 :',grade)
print('평균 :',average)

print('성명 : %s ' % name)
print('학번 : %d ' % no)
print('학년 : %d ' % year)
print('학점 : %s ' % grade)
print('평균 : %0.2f ' % average)

print("이름 : %s, 학년 : %d" %(name,year))
print(format(average,'10.2f'))
print(format(average,'0.2f'))

kor=90
eng=80
math=80
total=kor+eng+math
average=total/3
print('총점: %d, 평균: %.2f' %(total,average))


kor=90
eng=80
math=80
a=kor+eng+math
b=a/3
print('총점: %d, 평균: %.2f' %(a,b))

kor = 90
eng = 80
math = 80
sum = kor+eng+math
ave = sum/3

print('총점: '+format(sum, 'd')+', '+'평균: '+format(ave, '.2f'))


INT_Rate=0.03
deposit=10000
interest=deposit*INT_Rate
balance=deposit+interest
print(balance)
print(int(balance))

print(format(int(balance),','))

kor=90
eng=80
math=80
a=kor+eng+math
b=a/3
print('총점: %d, 평균: %.2f%%' %(a,b))

a=1+2+3 \
   +4+5
print(a)
b=(2+3+5
    +8)
print(b)
print("안녕하십니까"
      "난 민형이라 하오"
      "만나서 매우 반갑소")
print("안녕하십니까 \n 난 민형이라 하오\t만나서 매우 반갑소")

print("c:\PythonStudy\name")
print(r"c:\PythonStudy\name") #\n은 뛰어쓰기로 인식되므로 r을 이용해 없애자

print('first',end='@')
print('second')
'''
print('%50.1f' %2.555555)

print('%05d' % 543)
