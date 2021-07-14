import sys
bmodule=sys.builtin_module_names
print(bmodule)

# ('_abc', '_ast', '_bisect', '_blake2', '_codecs',
#  '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp',
#  '_codecs_kr', '_codecs_tw', '_collections', '_contextvars',
#  '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io','_json',
#  '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode',
#  '_operator', '_peg_parser', '_pickle', '_random', '_sha1', '_sha256',
#  '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string',
#  '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref',
#  '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii',
#  'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal',
#  'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype','zlib')

#dir(__builins__) 이용하면 더 많은 것을 찾을 수 있다.

#module 참조 : import
import random
import random as rd       #별명을 지정
from random import randint

# random.randint(1,10)
# rd.randint(1,10)
print(randint(1,10))