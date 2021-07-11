#생일 입력(연/월/일) : 1998/9/20
#당신은 1998년에 태어나셨군요
#생인은 9월 20일 이네요.
'''
a=input("생일 입력(연/월/일) : ")
bir=a.split('/')
print('당신은 %s년에 태어나셨군요' %bir[0])
print('생일은 %s월 %s일 이네요' %(bir[1],bir[2]))
'''

#주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하시오.
#split 이용하여 분리
#첫번째 분리된 결과는 리스트 형태로 주어지므로 반복문 for을 사용하여 다음 분리때 활용

data="{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
b=data.split(',')
sum=0                           #초기값을 지정하는 걸 정말 못한다ㅠ 이것때문에 오답 증가.
for n in range(len(b)):
    c=b[n]
    sum += int(c[4:6])
    avg=sum/5
print(sum,avg)                  #print 위치에 따라 답이 달라지기도 한다.

data="{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
b=data.split(',')
sum=0                           #초기값을 지정하는 걸 정말 못한다ㅠ 이것때문에 오답 증가.
for n in range(5):
    c=b[n]
    sum += int(c[4:6])
    avg=sum/5
    print(c)
print(sum,avg)                  #print 위치에 따라 답이 달라지기도 한다.

sum = 0
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
dataL = data.split(',')
for i in range(len(dataL)):
    score = dataL[i][4:6]
    sum += int(score)
avg = sum / len(dataL)
print("총점 :",sum,",합 :",avg)
