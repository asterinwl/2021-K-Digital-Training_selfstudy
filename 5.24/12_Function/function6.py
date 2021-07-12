#팩토리얼 계산 함수
#n!=n*(n-1)*...*3*2*1

def factorial(n):
    a=n
    for i in range(a-1,0,-1):
        a*=i
    return a
print(factorial(3))


def factorial(n):
    n = int(n)
    n *= n-1
    print(n)
print(factorial(5))

#재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

#f(4) 4*f(3) 4*3*f(2) 4*3*2*f(1) 4*3*2*1

n = int(input('n = '))


def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)

    return print(f)

factorial(n)
