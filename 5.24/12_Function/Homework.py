
def print_coin(coin):
    print(coin)
print_coin('비트코인')
print('---------')

for i in range(100) :          #i대신 _도 가능하다.
    print_coin("비트코인")
print('---------')

def print_coins(coins):
    for i in range(100):
        print(coins)
print_coins('비트코인')
print('---------')

# hello()
# def hello():
#  print("Hi")
# 첫 문장의 hello()는 list라는 것만 있을 뿐 안에 요소가 없으므로 지정되지 않음이라고 뜬다.
# list지정후 함수를 지정했으므로 첫 번째에는 hello에는 함수가 반영되지 않는다.

def message() :
 print("A")
 print("B")
message()
print("C")
message()
print('---------')

print("A")
def message() :
 print("B")
print("A")
print("C")
message()
print('---------')

print("A")
def messages1() :
 print("B")
print("C")
def messages2() :
 print("D")
messages1()
print("E")
messages2()
print('---------')

def message1() :
 print("A")
def message2() :
 print("B")
 message1()
message2()
print('---------')

def message1() :
 print("A")
def message2() :
 print("B")
def message3() :
 for i in range (3) :
  message2()
  print("C")
 message1()
message3()