'''
#딕셔너리 dictionary
#키와 값으로 구성 { 키1:값1, 키2:값2, .... }
#키의 값은 유일해야하므로 중복된 경우는 오류가 발생

#딕셔너리 만들기
d={}                  #d=dict()로도 딕셔너리를 만들 수 있음.
d={1:'a',2:'b',3:'c'} #item
print(d)
print(type(d))

#딕셔너리 요소 접근
print(d[1])

d2={'name':'Lee','tel':'010-111-1111'}
print(d2['name'])

#딕셔너리에 요소 추가
d[4]='f'
print(d)

d2['address']='서울시 강남구'
print(d2)

d3={'name':'daum',
    'ur1':'www.daum.net',
    'userid':'dm',
    'pw' : 1234 }

#key(),values(),items()

d3_Key=d3.keys()
print(type(d3_Key))
print(d3_Key)
print(list(d3_Key))

d3_values=d3.values()
print(list(d3_values))

d3_items=d3.items()
print(d3_items)
print(list(d3_items)[0])

for key in d3.keys():
    print(key)

for value in d3.values():
    print(value)

for item in d3.items():
    print(item)

print(d3['name'])
print(d3.get('url'))
print(d3.get('add','not exist'))  #Nome 대신 not exist 를 표시해줘라.

k='link'

if d3.get(k) is None :
    print((k + '에 대한 데이터가 없음'))

#in/not in
print('link' in d3)
print('link' not in d3)

print(dir(d3))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__',
#  '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__',
#  '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items',
#  'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(d3.popitem())    #마지막꺼를 꺼내옴
print(d3)              #마지막꺼를 삭제함

hey={x:x**2 for x in {2,4,6}}        #dictionary 생성
print(hey)

hey1=[x**2 for x in (2,4,6)]         #list 생성
print(hey1)

for key, val in d3.items() :
    print('%s : %s' %(key,val))

students = {1:[80,86,60],
            2:[87,90,30]
            3:[]}
endDict={}
endDict['dog']='개'
endDict['cat']='고양이'

#리스트와 딕셔너리는 변경 가능, 하지만 튜플은 변경 불가능
'''

d1={}
key=input('키입력')
d1[key]='개'
print(d1)
