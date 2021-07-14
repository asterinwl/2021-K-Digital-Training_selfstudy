#any(), all()
print(all([0,1,2,3]))
print(any([0,1,0]))
print(any([0,'',0]))
print(any([0,[],0]))

#ascii code value : chr(x)
print(chr(65))
print(chr(97))

#ord(c)
print(ord('a'))
print(ord('\n'))
print(ord(' ')) #뛰어쓰기 꼭 해야한다.
print(ord('\t'))
print(ord('\\'))

#bin(),oct(),hex(),int(),float(),str()

#divmod(a,b)
print(divmod(7,3))  #몫 / 나머지
print(divmod(9,3))

#eval(expression)
print(eval('13.5'))
print(type(eval('13.5')))
print(eval('3+5'))
print(type(eval('3+5')))  #유형을 ' '를 벗겨서 측정해줌.

#help 이게 어떤 함수인지 알려주는 것이다.
help(print)
help(map)
help(sum)