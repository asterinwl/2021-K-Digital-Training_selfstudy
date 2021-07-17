a=input("저장 1, 출력 2, 종료 q : ")
if a=='1':
    b=input("멤버 명단을 저장할 파일명을 입력하세요. : ")
    c=open(b,'w',encoding='utf-8')
    d = input('멤버를 입력하세요.(종료는 q) : ')
    while True:
        if d!='q' :
            c.write(d)
            d = input('멤버를 입력하세요.(종료는 q) : ')
        else:
            break
        c.close()
elif a=='2':
    b=input("멤버 명단을 저장할 파일명을 입력하세요. : ")
