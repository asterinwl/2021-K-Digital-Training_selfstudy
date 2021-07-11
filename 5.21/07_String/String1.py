#문자열의 기본 형식과 이해
crawling="Data crawling is fun."
parsing='Data parsing is also fun.'

print(crawling)
print(parsing)

print(type(crawling))
print(type(parsing))

'''
PI = 3.1415
r=10
result="반지름 " + str(PI) + "인 원의 넓이는" + str(PI*r*r)
print(result)
print('hello'*3)
'''

#slicing : 문자열의 일부분을 추출
#string[0] : 인덱스 0번째 문자(첫 번째 문자)
#string[-1] : 마지막 문자
print(crawling[-1])
print(crawling[0])
print(crawling[1:5])
print(crawling[:-1])
print(crawling[-1:])
print(crawling[:])
print(crawling[0:10])