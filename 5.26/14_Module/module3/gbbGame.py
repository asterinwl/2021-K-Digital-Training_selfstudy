
def gbb_game(you_n):
    from random import randint
    COM=randint(1,3)
    if COM-you_n==-2 or COM-you_n==1 :
        print('컴퓨터가 이겼습니다.')
    elif COM-you_n==0 :
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다')
    print("COM : ", COM)
    return you_n

def input_num():
    a=int(input("YOU 입력 (1:가위, 2:바위 3:보) : "))
    gbb_game(a)
