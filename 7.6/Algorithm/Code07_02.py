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

def deQueue(data) :
    global SIZE,queue,front,rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return
    front +=1
    queue[front]=data
    queue[front]=None
    return data

#전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

#메인 코드부
queue=['화사','솔라','문별','휘인','선미']
front=-1
rear=4

print('큐 꽉?',isQueueFull())
print('큐 꽉?',isQueueEmpty())
print()

print(queue)
enQueue('화사')