#calculator module

#계산기 함수 : add(x,y), sub(x,y), mul(x,y), div(x,y)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

#__name__ 변수 사용 : '__main()__'
print('Here id Calculator module')  #다른 곳에서 참조해도 이 값이 나옴. 왜냐하면 이것은 중요한 요소이니까.

print('__name__:',__name__)
if __name__=='__main__':
    print('check it')
    print('__name__:',__name__)      #이 경우에는 참조해도 이 값이 나오지 않음. main에서만 뜨게 된다는 의미.