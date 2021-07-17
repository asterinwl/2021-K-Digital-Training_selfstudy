#파일 내에서 검색
#seek(offset, whence) 함수

print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')    #encoding은 Tab 사용하지 말자
f.seek(0,0)  #시작위치는 0행,0열
lines=f.readlines()
print(lines)
f.close()

print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')
f.seek(1,0)  #시작위치는 0행,1열
lines=f.readlines()
print(lines)
f.close()

print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')
f.seek(7,0)  #시작위치는 1행,0열
lines=f.readlines()
print(lines)
f.close()

print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')
f.seek(14,0)  #시작위치는 2행,0열
lines=f.readlines()
print(lines)
f.close()

'''
print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')
f.seek(15,0)  #한글이라서 가에서 반반이 되므로 오류가 생긴다. / 한글은 3바이트를 먹는다.
lines=f.readlines()
print(lines)
f.close()
'''

print('-----파일 내에서 검색 seek()-----')
f=open('test2.txt','r',encoding='utf-8')
f.seek(17,0)
lines=f.readlines()
print(lines)
f.close()

print('-----파일 내에서 검색 seek()-----')
f=open('test2_utf16.txt','r',encoding='utf-16')
f.seek(16,0)  #시작위치는 2행,0열
lines=f.readlines()
print(lines)
f.close()

#한글은 utf8은 3byte, utf16이 2byte라고 합니다
