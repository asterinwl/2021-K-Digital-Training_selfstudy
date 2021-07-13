
def multi(num1,num2) :
    ans=num1*num2
    return ans
n1=int(input("첫 번째 수 : "))
n2=int(input("두 번째 수 : "))
print("두 수의 곱은 : ", multi(n1,n2))
print('-'*30)


a='ticker'
print(a)
def change(word) :
    words=word.upper()
    return words
print(change(a))
print('-'*30)



def pickup_even(number) :
    num=[]
    for x in number :
        if x % 2 == 0 :
            num.append(x)
    return num
print(pickup_even([1,2,3,4,5,6]))



