
score=55
if score >= 60 :
    print("합격이다.")
else :
    if score >= 40 :
        print("불합격 이지만 과락은 아닙니다.")
    else :
        print("불합격 이면서 과락입니다.")

score=55
if score >= 60 :
    print("합격이다.")
elif score >= 40 :
    print("불합격 이지만 과락은 아닙니다.")
else :
    print("불합격 이면서 과락입니다.")


inStr, outStr = 'Python', ''
strLen = len(inStr)
for i in range(0, strLen):
    outStr += ( inStr[strLen - (i+1)])
print('내용을 거꾸로 출력 : %s' % outStr)

myData = { 1, 1, 1, 2, 2, 3, 3, 3 }
print(myData)

months = ['January', 'February', 'March']
months.append('April')
print(months)


fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')

print(fruits[1:4])


print(6/3)
print(6%3)

for i in range(1,10) :
    for k in range (0, 10, 2) :
        print("파이썬 정말 재미있어요~")