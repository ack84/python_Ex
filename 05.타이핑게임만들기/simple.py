from operator import index
import time
import random
WORD_LIST = [
    "남박사는 학생이다.",
    "손박사는 손박사이다.", 
    "지금은 지금의 연속이다."
]

random.shuffle(WORD_LIST)

for question in WORD_LIST:
    start_time = time.time()
    user_input = str(input (question + '\n')).strip()
    end_time = time.time() - start_time

    #종료 명령어 
    if user_input == "exit":
        break
    correct = 0

    #입력받은 문자를 index를 부여
    for index,  input_char in enumerate(user_input):
        #입력받은 글자수가 문제수보다 큰지 체크
        if index > len(question): 
            break
        if input_char == question[index]:
            correct += 1 

    total_len = len(question)
    input_char = correct / total_len * 100
    wrongPer = (total_len - correct) / total_len * 100
    speed = (correct / end_time ) * 60

    print ("속도 : {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed, input_char, wrongPer))
 