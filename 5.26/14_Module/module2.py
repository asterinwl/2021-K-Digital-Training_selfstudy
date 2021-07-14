#calculator module 참조
import calculator

a= calculator.add(9, 8)
print(a)
print(calculator.mul(10,5))

#form calculator import div,add,mul

import showinfo
showinfo.show_name()    #오류가 생긴다.
                        #다른 곳에서 생긴 파일이므로 오류가 생기는 것이다.
from calculator import *    #calculator를 일일히 붙이기 싫을 경우
print(add(5,1))

from showinfo import *
show_name()
show_phone()
print('module2.py __name__ : ', __name__)

import moduleMain

print(moduleMain.getName())
moduleMain.main()