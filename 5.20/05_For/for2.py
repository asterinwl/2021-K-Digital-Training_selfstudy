#1~10 사이의 수를 더하고 더한 결과 출력
total = 0
for n in range(11):
    total = total+n      #total += n 도 같음
print('합은 %d' %total)
print('\n--------------')

total = 0
for n in range(11):
    total += n
print('합은 %d' %total)