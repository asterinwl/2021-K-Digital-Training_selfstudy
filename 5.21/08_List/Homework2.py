

a=int(input("학생 수 입력 : "))
c=[]
sum=over=0
for i in range(1,a+1) :
   b=input("학생%d 수 입력 : " %i)
   sum+=int(b)
   c.append(b)
   if int(b)>=80 :
      over+=1
print('총점 : %d' %sum)
print('평균 : %.2f' %(sum/a))
print('80점 이상 학생 : %d명' %over)
c.sort(reverse=True)
print('점수 내림차순 정렬 : ',c)
print('----------------------------------')


four=['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
mean=['잘못을 고치고 옳은 길에 들어섬','죽을 고비를 여러번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람',
      '아무짝에나 쓸모 없는 것','고통과 즐거움은 함께 한다','미리 준비해두면 근심 걱정이 없다',
      '사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
      '생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤 일을 이룰 수 없다']

print("사자성어 맞추기 게임을 시작합니다")
print('---------------------------------')

while True :                                  #while True가 앞에 위치해야 오류가 안생긴다
    from random import randint                #이 경우 모든 경우가 랜덤하게 나온다.
    A=randint(0,9)                            #randint가 while True 앞에 있으면 같은 문장이 계속 나온다.
    print(mean[A])
    B=input("이 말의 사자성어는? : ")
    print(' ')
    if B==four[A] :
        print("맞습니다..게임을 종료합니다.")
        break
    else :
        print("틀렸습니다...다시 도전 !")

'''                                           
from random import randint                   #기존에 푼 식
A=randint(0,9)                               #이유는 모르겠지만 A가 고정되지 않고 랜덤하게 부과된다.
print(mean[A])                             
B=input("이 말의 사자성어는? : ")
print(' ')
    while True
        if B==four[A] :
        print("맞습니다..게임을 종료합니다.")
        break
    else :
        print("틀렸습니다...다시 도전 !")
        print(' ')
        print(mean[A])
        
'''