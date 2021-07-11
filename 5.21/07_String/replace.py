#replace()
text = 'happy king'
text = text.replace('happy','queen')
print(text)

#대문자/소문자 변환
#upper() lower() capitalize() title()
text='java programming if Fun'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

#공백문자 제거 strip(), lstrip(), rstrip()
text='java programming if Fun'
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.rstrip()+'---')