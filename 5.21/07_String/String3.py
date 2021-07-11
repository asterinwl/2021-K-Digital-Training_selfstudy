#string 관련 함수들
#Len():문자열의 길이
string='Python Programming'
n=len(string)
print(n)

#count():문자열에서 찾고자하는 문자(열)의 갯수
print(string.count('m'))
print(string.count('ing'))

#find():특정문자열이 존재여부에 따라 위치나 -1(없는 경우)
print(string.find('ing'))
print(string.find('ong'))

#index():특정문자열이 존재여부에 따라 위치나 오류(없는 경우)
print(string.index('ing'))
print(string.index('ong'))
