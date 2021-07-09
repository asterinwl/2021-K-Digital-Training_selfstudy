#입력한 정수가 양수, 음수, 0 판별하여 출력
number=int(input('정수입력:'))

if(number>0):
    print('양수')
else:
    if(number<0):
        print('음수')
    else:
        print('0')

if(number>0):
    print('양수')   #뛰어쓰기도 신경써야한다.
elif(number<0):
    print('음수')
else:
    print('0')