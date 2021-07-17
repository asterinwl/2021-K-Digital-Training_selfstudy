'''
#파일생성 : 파일명만 적기
f=open('c://PythonStudy/file1.txt','w')          #절대경로
f.close()

# f=open('file1.txt','w')
# f=close()                   :상대경로 16_File->file1.py 밑의 txt로 나옴.

#경로 수정 : 디렉토리 존재하지 않는 경우
f=open('c://ythonStudy/file1.txt','w')
f.close()
No such file or directory: 'c://ythonStudy/file1.txt

#디렉토리 경로 설정시 '\' 사용하면 오류 발생 =>\\ 또는 /
f=open('c:\ythonStudy\file1.txt','w')
f.close()
Invalid argument: 'c:\\ythonStudy\x0cile1.txt'


#상대경로 표현
f=open("../File.txt","w")
f.close()
'''