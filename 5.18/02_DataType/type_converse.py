'''
#print("나는 현재 나이가 "+str(23)+"살 입니다.")

num=input('숫자를 입력하세요 : ')

#print(num+100)
#print(int(num)+100)

print(int('123',8))    # 이 친구는 8진수이다.
print(int('123',16))   # 이 친구는 16진수이다.

print(float(num)+100)
'''
a=input('첫 번째 수를 입력하세요 : ')
b=input('두 번째 수를 입력하세요 : ')
total=int(a)+int(b)  #해당 문자가 숫자인지 글자인지 확실히 알아야하므로 꼭 int를 언급해준다.
average=total/2
print('두 수의 합은'+str(total)+' 이고 평균은 '+str(average)+'입니다')
print('두 수의 합은 %d, 평균은 %.0f'%(total,average))
print('두 수의 합은 {0}, 평균은 {1}'.format(total,average))
print('두 수의 합은 {0:d}, 평균은 {1:0.0f}'.format(total,average)) #합은 정수의 값으로 평균은 첫자리부터 쓰되 소수점은 없는 상태로
print('두 수의 평균은 {1}, 합은 {0}'.format(total,average))
print('두 수의 합은 {}, 평균은 {}'.format(total,average)) #{}안에 숫자를 적지 않으면 임의적으로 0과 1로 만들어준다.