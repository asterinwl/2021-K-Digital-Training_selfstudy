#파일에 쓰기 : 파일을 쓰기 모드(w)로 열고, 파일객체의 write() 함수를 이용하여 파일에 출력(기록)


# data='hello'
# f=open('file2.txt','a') #파일객체 f
# f.write(data)
# f.close()

data='안녕하세요'
f=open('file2.txt','w',encoding='utf-8')
f.write(data)
f.close()
#utf-8 형식으로 저장해야지 한글은 깨지지 않음.