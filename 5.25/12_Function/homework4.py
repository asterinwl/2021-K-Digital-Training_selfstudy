def pickup_even():
 numbers = []
 num_1 = int(input("표본 숫자 개수 : "))
 for x in range(num_1):
    number = int(input("숫자 입력 : "))
    if number % 2 ==0 :
        numbers.append(number)
 return numbers
print(pickup_even())
