def findMinIdx(ary):
    minIdx=0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]) :
            minIdx=i
    return  minIdx

import random
before=[chr(random.randint(44032,55203)) for _ in range(30)]
#ord(가)=44032 ord(힣)=55203
after =[]

##메인 코드부
print('정렬전-->',before)

for _ in range(len(before)):
    minPos=findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬후-->',after)