#함수 선언부
def isQueueFull():
    global SIZE,queue,front,rear
    if (rear==SIZE-1) :
        return True
    else :
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front==rear) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE,queue,front,rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear +=1
    queue[rear]=data

def deQueue() :
    global SIZE,queue,front,rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return
    front +=1
    queue[front]=None
    return

#전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


print(queue)
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
enQueue('송가인')
print(queue)
retData=deQueue()
print(retData)
retData=deQueue()
print(retData)
retData=deQueue()
print(retData)
retData=deQueue()
print(retData)
retData=deQueue()
print(retData)
print(queue)
enQueue('재남')