def isStackFull() :
    global SIZE,stack,top
    if (top>=SIZE-1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print("스텍 꽉!")
        return
    top +=1
    stack[top]=data

def isStackEmpty() :
    global SIZE, stack, top
    if top<0:
        return True
    else :
        return False


def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print("스텍 비어있음")
    else :
        del(stack[top])
        top -=1

SIZE=5
stack=['커피','녹차','꿀물','콜라','환타']
top=4

print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()