crawling="Data crawling is fun"
print(crawling.find('i'))
print(crawling.rfind('i'))       #오른쪽 부터 찾자.
print(crawling.rfind('i',1,9))   #1에서 9까지에서 i를 찾기
print('---------------------')

print(crawling.index('i'))
print(crawling.rindex('i'))
#print(crawling.index('i',1,9))  #index는 해당값이 없는 경우 오류로 뜬다.
print('---------------------')

#split():지정된 문자로 문자열을 분할함. 리스트 형식으로
token=crawling.split()
print(token)                     #공백을 이용하여 쪼개준다.
print('---------------------')

names='Lee,Kim,Choi,kang'
print(names.split())
print(names.split(','))
nameL=names.split(',')
for n in nameL:
    print(n)
for i in range(len(nameL)) :
    print(nameL[i])
print('---------------------')

#문자열의 요소 하나씩 출력
for c in crawling :
    print(c)