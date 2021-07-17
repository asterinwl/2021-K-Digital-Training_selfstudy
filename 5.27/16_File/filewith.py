#with 문으로 파일 열기

with open('test3.txt', 'w') as f :
    f.write('hello')


filename='test4.txt'
data='나는 파이썬을 배우고 있어요'\
    '매우 여려워요' \
     '하지만 해야줘 머'

with open(filename, 'w', encoding='utf-8') as f:
    f.write(data)