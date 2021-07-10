#이름 리스트에 해당하는 이름이 있는 경우 이름이 있음을 출력한다.
names = ['홍길동','이몽룡','성춘향','변학도']

inputName = input("이름 입력 :")

for name in names :
    if inputName == name :
        print("명단에 있습니다.")
        break
    else :
        print("명단에 없습니다.")

 # 이름을 쓰면 4번 반복한다. '이몽룡'인 경우 없음/ 있음 2번 나오고 박지성이면 없음 4번 나온다.

names = ['홍길동', '이몽룡', '성춘향', '변학도']

inputName = input("이름 입력 :")

for name in names:
    if inputName == name:
         flag=True
         break
    else :
         flag=False

if flag:                            #이미 flag에 참/거짓이 들어가있으므로 flag==True 안해도 된다.
    print("명단에 있습니다.")
else:
    print("명단에 없습니다.")
