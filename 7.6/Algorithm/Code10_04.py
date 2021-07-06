def CountDown(n) :
    if n==0 :
        print('발사 시작!')
    else :
        print(n)
        CountDown(n-1)

CountDown(5)
print()


def star(num) :
    if num==6 :
        print(" ")
    else :
        print('★'* num)
        star(num+1)

star(1)


for i in range(2,10):
    def table(number) :
        if number==10 :
            print(" ")
        else :
            print(i, "X", number, "=", i * number)
            table(number + 1)

    table(1)


def multiply(a,b):
    if b!=0:
        print(pow(a,b))
        multiply(a,b-1)
multiply(2,4)
print()


def Sum(c):
    d=len(c)
    if d>1:
        print(sum(c))
        c=c[:-1]
        Sum(c)
        return ' '     #return을 주지 않으면 맨마지막에 None 이 나온다.
    else :             #return에 Sum(c)를 넣으면 21이 뜬다.(c=c[:-1]때문)
        c=c[0]         #그 이유 때문에 return ' '을 넣었다.
        print(c)

print(Sum([5,3,7,2,1,3,5]))