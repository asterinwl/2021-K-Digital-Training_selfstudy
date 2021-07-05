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


SIZE=5
stack=['커피','녹차','꿀물','콜라','환타']
top=3       #3번째 자리인 콜라까지만 담기

print(stack)
push('주스')
print(stack)
push('사이다')
print(stack)