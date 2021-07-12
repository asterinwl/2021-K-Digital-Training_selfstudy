my_variable=()
print(type(my_variable))

#t = (1, 2, 3)
#t[0] = 'a'
#tuble에는 새로운 요소를 집어넣을 수 없어서 오류가 생긴다.

hi=tuple()
hi=(1,)
print(type(hi))
print(*hi)

# num = tuple()
# list(num)
# num.append(1)
# num=tuple(num)
# tuple(num)

t=1,2,3,4
print(type(t))

t=('a','b','c')
tl=list(t)
tl[0]='A'
t=tuple(tl)
print(t)
print(type(t))

interest=('삼성전자','LG전자','SK Hynix')
interestl=list(interest)
print(interestl)
print(type(interestl))

interest=['삼성전자','LG전자','SK Hynix']
interestt=tuple(interest)
print(interestt)
print(type(interestt))

partyA={"Park","Kim","Lee"}
partyB={"Park","길동","몽룡"}

print("1)파티에 참석한 모든 사람은?" , *(partyA | partyB))
print("2)2개의 파티에 모두 참석한 사람은?" , *(partyA&partyB))
print("3)파티 A에만 참석한 사람", *(partyA-partyB))
print("4)파티 B에만 참석한 사람" , *(partyB-partyA))



