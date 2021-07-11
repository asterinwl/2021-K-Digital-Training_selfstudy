#리스트의 확장 : extend() : append() insert()
a=[3,6,0,-4,1]
b=[40,30,20,50]
# a.append(b)
# print(a)
# a.insert(2,b)
# print(a)
a.extend(b)
print(a)            #b의 리스트의 리스트가 아니라 그냥 들어감.
