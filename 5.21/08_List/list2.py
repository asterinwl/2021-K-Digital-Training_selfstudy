#리스트의 복사

#얕은 복사 : copy() list() deepcopy()

scores = [65, 70, 90, 89, 78]
value=scores

print('scores : ', scores)
print('value : ',value)

scores[3]=98
print('scores 값변경 :',scores)
print('value : ', value)            #scores 값 변경하니 value 값도 변경

value[0]=100
print('scores : ', scores)
print('value : ',value)

value2=scores.copy()              #value2 값이 바뀌지 않음.
print('value2 : ',value2)
scores[0]=50
print('scores : ', scores)
print('value : ',value)
print('value2 : ',value2)

#깊은 복사
value3=list(scores)               #value3 값이 바뀌지 않음.
print('value3 : ',value3)
scores[0]=150
print('scores : ', scores)
print('value : ',value)
print('value3 : ',value3)

import copy

value4 =copy.deepcopy(scores)
scores[2]=200
print('scores : ', scores)
print('value4',value4)