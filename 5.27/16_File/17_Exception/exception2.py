#예외 발생 상황

#division by zero
#print(10/0)
print('1')
try:
    print(10/0)
except:
    print('오류가 발생')
finally:
    print('나누기')
print('2')

try:
    print(10/0)
except ZeroDivisionError:           #해당되는 에러가 나올 경우에는
    print('0으로 나눌 수 없습니다.')
finally:
    print('나누기')
print('3')

try:
    print(10/0)
except ZeroDivisionError as e:           #해당되는 에러가 나올 경우에는
    print('0으로 나눌 수 없습니다.', e)
finally:
    print('나누기')
print('4')

#TypeError: can only concatenate str (not "int") to str
#print('age='+23)

try:
    print('age=' + 23)
except Exception as e:                   #에러메시지가 나온다.
    print(e)
print('5')

try:
    print(10/0)
    print('age='+23)
except ZeroDivisionError as e:           #제일 처음에 나오는 값만 반환된다.
    print('0으로 나눌 수 없습니다.', e)
except Exception as e:
    print(e)
print('6')

try:
    print('age='+23)
    print(10/0)
except ZeroDivisionError as e:           #제일 처음에 나오는 값만 반환된다.
    print('0으로 나눌 수 없습니다.', e)
except Exception as e:
    print(e)
print('7')

try:
    num=int(input('input number :'))
except ValueError:
    print('숫자가 아닙니다.')
else:
    print(num)
finally:
    print('종료')           #오류든 아니든 항상 나온다.
print('8')

try:
    f=open('testex.txt','r')
except FileNotFoundError:
    pass
else:
    data=f.read()
    print(data)
    f.close()
finally:
    print('종료')           #오류든 아니든 항상 나온다.


#NameError: name 'x' is not defined
#print(x)

#ValueError: incomplete format
# a=100
# print("%d%" %a)

#SyntaxError: invalid syntax
# if x>10
#     print('KIM')

#IndexError: list index out of range
# a=[1,2,3]
# print(a[3])

#unboundLocalError
# def add():
#     a +=1

#ModuleNotFoundError: No module named 'modd'
#import modd
