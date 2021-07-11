#index() 메소드 : 해당되는 값의 위치를 알려주는 것.

a=[3,6,0,-4,1]
b=a.index(-4)
print(b)

#in/not in
if 2 in a:
    print('Exist')
else :
    print('Not exist')

if 2 not in a:
    print('Not exist')
else :
    print('Exist')