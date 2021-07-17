#readlines() 함수 이용하여 파일 읽어오기
#readlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#              ['...\n','...\n','...\n',...,'...\n']
#read() : 내용 전체를 한 문자열로 반환 ''' '''

# 파일 전체 읽기
# f=open('test.txt','r')
# myL=[]
# while True:
#     lines = f.readlines()
#     if(lines==''):
#         break
#     myL.append(lines)
# f.close()
# print(myL)

# f=open('test.txt','r')
# lines=f.readlines()
# print(lines)
# f.close()

#readlines()로 읽은 내용을 한 줄씩 출력하기

# f = open('test.txt', 'r')
# line = f.readlines()
# for i in range(len(line)):
#     print(line[i], end='')
# f.close()
#
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()