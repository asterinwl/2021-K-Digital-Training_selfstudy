def isStackFull() :
    global SIZE,stack,top
    if (top>=SIZE-1) :
        return True
    else :
        return False

SIZE=5
stack=['커피','녹차','꿀물','콜라','환타']
top=4

print("스텍 꽉?",isStackFull())