import random
from this import d

#number 는 임의로 뽑은 숫자
#numbers에 list형태로 담기
numbers = []
number = str(random.randint(0,9))

# 맞춰야 할 숫자(number)를 3개 랜덤으로 뽑아서 numbers에 append하기 
for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

count_strike = 0
count_ball = 0

while count_strike < 3:
    count_strike = 0
    count_ball = 0

    num = str(input("숫자 3자리를 입력하세요.> "))
    if len(num) == 3:
        for i in range(0,3):
            for j in range(0,3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                if num[i] == numbers[j] and i != j:
                    count_ball += 1

        if count_strike == 0 and count_ball == 0:
            print("3아웃 !!!")
        else: 
            output =""
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += " {} 볼".format(count_ball)

            print(output.strip())
print ("게임성공")
d
