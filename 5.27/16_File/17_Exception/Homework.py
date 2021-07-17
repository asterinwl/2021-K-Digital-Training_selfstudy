print("1번")
a=lambda x,y:x**y
print(a(2,3))
print("")

print("2번")
print(list(map(lambda x:x**2,[1,2,3,4,5])))
print("")

print("3번")
print("3")
print("")

print("4번")
print("3")
print("")

print("5번")
print("3")
print("")

print("6번")
print("import fah_coverter")
print("")

print("7번")
print("game 패키지를 library root로 지정한다.")
print("")

print("8번")
print("가-'a'  나-write")
print("")

print("9번")
print("가-'w'  나-'a' 다-'r'")
print("")

print("10번")
print("import calculator")
print("")

print("11번")
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally: print("종료되었습니다.")
print("7\n3\n2\n1\n1\n1")
print("종료되었습니다.")
print("")

print("12번")
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break
print("pop from empty list : 정답은 맞았는데 한 글자씩 나올줄은 몰랐어요.")
print("")

print("13번")
# alist = ["a", "1", "c"]
# blist = ["b", "2", "d"]
# for a, b in enumerate(zip(alist, blist)): print(b[a])
# alist = ["a", "1", "c"]
# blist = ["b", "2", "d"]
# for a, b in enumerate(zip(alist, blist)): print(a/int(b[0]))
print("4")
print("")

print("14번")
print("2")
print("")

print("15번")
print("2")
print("")

print("16번")
import random
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다.")
guess_number(answer)
print("내가 적은 정수 값이 answer가 같으면 정답! 아니면 틀렸습니다. 만약 정수를 적지 않으면 숫자가 아닙니다.")
print("")

print("17번")
print("1-NameError")
print("2-FileNotFoundError")
print("3-ValueError")
print("4-SyntaxError")
print("")

print("18번")
for i in range(3):
    try:
        print(i, 3// i)
    except ZeroDivisionError:
        print("Not divided by 0")
print("Not divided by 0")
print("1 3")
print("2 1")
print("")

print("19번")
print("with open('i_have_a_dream.txt', 'w')")
print("")