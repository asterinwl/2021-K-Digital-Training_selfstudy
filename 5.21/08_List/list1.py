#리스트의 기본 개념
intL=[1,3,2,10]
floatL=[1.5,3.2,5.4]
nameL=['홍길동','성춘향','변학도','방자']
numL=[1,3,4,[1,2]]
samL=[1,3,.5,'하하']

# print(intL)
# print(type(intL))
# print(numL)
# print(samL)
#
# #인덱싱 & 슬라이싱
# print(nameL[-1])
# print(nameL[:])
# print(nameL[1:3])
# print(numL[-1],[0])
#
# # allL=[] #빈 리스트 생성    ctrl+/ = 모두 각주 처리
# # allL=list()
# # print(allL)
#
# allL=[intL,floatL,nameL,numL]
# print(allL)
# print(allL[-1][-1][0])
# print(nameL[:-1])
# print(nameL[-1:])
# print(nameL[-1])
# n=len(nameL)
# print(nameL[:n])
#
# #리스트의 +,* 연산
# sumL=numL+samL
# print(sumL)
# print(numL*3)

#리스트의 내용 변경
print(numL)
numL[3] =10
print(numL)
numL[2:4]=[]
print((numL))

'''
for i in numL :
    print(i)

for i in range(len(numL)):
    print(numL[i])

a, b, c = floatL
print(a)
print(b)
print(c)
print('-------------------------------')

data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
dataL = data.split(',')
n=total=0
for i in dataL:
    id, score = i.split(":")
    score=int(score.split('}')[0])
    total +=score
    n +=1
print(total,total/n)
print('---------------------------------')
'''
