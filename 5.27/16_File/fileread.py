#readline() 함수 이용하여 파일 읽어오기
#readline() : 1개의 행씩 읽어 오기, 행 끝에 '\n'포함
#readlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#              ['...\n','...\n','...\n',...,'...\n']
#read() : 내용 전체를 한 문자열로 반환 ''' '''
'''
print('-----첫 번째 행 읽어오기-----')
# ANSI 형식으로 저장된 파일 읽기
# f=open('test.txt','r')
# line=f.readline()
# print(line)
# f.close()

# 인코딩 utf-8 로 지정하여 해결
# f=open('test.txt','r',encoding='utf-8')
# line=f.readline()
# print(line)
# f.close()

f=open('test.txt','r')
line=f.readline()
print(line,end='')
line=f.readline()
print(line)
f.close()
'''

print('-----파일 전체 읽기-----')
f = open('test.txt','r')
while 1:
    try:
        line = f.readline()
        print(line, end="")
    except Exception:
        break
f.close()


'''
print('-----파일 전체 읽기-----')

f = open('test.txt', 'r')
line = f.readline()
print(line, end = '')
while True:
    line = f.readline()
    if(line == ''):
        break
    print(line, end = '')

f.close()
'''
