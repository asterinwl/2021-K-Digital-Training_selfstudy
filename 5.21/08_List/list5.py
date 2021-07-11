#리스트의 요소를 정렬 : sort(), reverse() / sorted() 함수
a=[3,6,0,-4,1]
 a.sort()
 print(a)
 a.sort(reverse=True)
 print(a)

#reverse() 메소드를 사용하지 않고 리스트를 역순으로 생성하여 출력하기
# for i in range(len(a)-1,0,-1) :
#
# b = []
# for i in range(len(a)):
#     # item=a.pop()
#     # print(item)
#     # b.append(item)
# print(b)

    #b.append(a.pop())

#sorted() 함수
# c=sorted(a)
# print(a)
# print(c)
#
# string=['Apple','banana','melon','apple','GRAPE']
# string.sort()
# print(string)
# string.sort(key=str.lower)
# print(string)
# string.sort(key=str.upper)
# print(string)
#
#
# #리스트의 요소 찾기 : index()
#
# #리스트 요소 중 큰 값(max()), 작은 값(min())
# print(max(a))
# print(min(a))
#
# print(max(string))
# print(min(string))
