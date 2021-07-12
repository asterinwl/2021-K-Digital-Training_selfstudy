print('1번')
students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92} ]
a=students[0]
b=students[1]
c=students[2]
d=students[3]
e=students[4]
f=students[5]
A=dict(a)
B=dict(b)
C=dict(c)
D=dict(d)
E=dict(e)
F=dict(f)
print("이름         총점       평균 ")
print("%s %10d %10.1f" %(A["name"],A["korean"]+A["math"]+A["english"],(A["korean"]+A["math"]+A["english"])/3))
print("%s %10d %10.1f" %(B["name"],B["korean"]+B["math"]+B["english"],(B["korean"]+B["math"]+B["english"])/3))
print("%s %10d %10.1f" %(C["name"],C["korean"]+C["math"]+C["english"],(C["korean"]+C["math"]+C["english"])/3))
print("%s %10d %10.1f" %(D["name"],D["korean"]+D["math"]+D["english"],(D["korean"]+D["math"]+D["english"])/3))
print("%s %10d %10.1f" %(E["name"],E["korean"]+E["math"]+E["english"],(E["korean"]+E["math"]+E["english"])/3))
print("%s %10d %10.1f" %(F["name"],F["korean"]+F["math"]+F["english"],(F["korean"]+F["math"]+F["english"])/3))

print('2번')
diction={}

while True :
    key = input("영어 단어 등록 (종료는 quit) : ")
    if  key=="quit" :
        print(" ")
        break
    elif key in diction :
        print(key + "는 이미 등록된 단어입니다.")
        print(" ")
    else :
        value = input(key + "의 뜻 입력 (종료는 quit) : ")
        print(" ")
        diction[key] = value

while True :
    word = input("검색할 단어 입력 (종료는 quit) : ")
    if word == "quit":
        print(" ")
        print("종료합니다.")
        break
    elif word not in diction:
        print(word + "는 사전에 없는 단어 입니다.")
        print(" ")
    else:
        print(word + "의 뜻은  " + diction[word] + "입니다.")
        print(" ")