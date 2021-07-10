#다중 for (중첩)
for y in range(3):
    for x in range(5):
        print(x, end=" ")
    print()                      #행이 y행 x열 사각형 모양으로
print('---------------------------------------')
for y in range(3):
    for x in range(5):
        print(x, end=" ")
print()                         #한 줄로
print('---------------------------------------')

for y in range(3):
    for x in range(1,5):
        print('%3s' %(x+y*4), end=" ")  #'%3s'는 문자가 들어가는 데 3자리수라는 의미
    print()
print('---------------------------------------')
a=0
for i in range(3):
    for j in range(4):
        a +=1
        print(a, end='\t')
    print()