#큐의 초기화
SIZE=5
queue=[None,None,None,None,None]
front=rear=-1

#데이터 삽입
rear +=1
queue[rear]='화사'
rear +=1
queue[rear]='솔라'
rear +=1
queue[rear]='문별'

print(queue)

#추출(삭제)
front +=1
data=queue[front]
queue[front]=None
print('추출-->',data)
front +=1
data=queue[front]
queue[front]=None
print('추출-->',data)
front +=1
data=queue[front]
queue[front]=None
print('추출-->',data)