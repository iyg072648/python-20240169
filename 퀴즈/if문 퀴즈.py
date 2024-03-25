#곱셈 퀴즈 프로그램
import random

score = 0

# result = int(input('3 * 6 = '))
# if result == 3 * 6:
#     score += 20
#     print("맞았습니다.")
# else:
#     print("틀렸습니다")

# result = int(input('7 * 8 = '))
# if result == 7 * 8:
#     score += 20
#     print("맞았습니다.")
# else:
#     print("틀렸습니다")
    
# result = int(input('2 * 9 = '))
# if result == 2 * 9:
#     score += 20
#     print("맞았습니다.")
# else:
#     print("틀렸습니다")
    
# result = int(input('6 * 4 = '))
# if result == 6 * 4:
#     score += 20
#     print("맞았습니다.")
# else:
#     print("틀렸습니다")
    
# result = int(input('9 * 3 = '))
# if result == 9 * 3:
#     score += 20
#     print("맞았습니다.")
# else:
#     print("틀렸습니다")

#for,random 변수를 통한 랜덤 문제 제출
# for i in range(5):
#     num1 = (random.randrange(1,10))
#     num2 = (random.randrange(1,10))
#     print(num1, '*', num2, '=')
#     result = int(input()) #어떻게 선언하는지 몰라서 print,input 따로 출력
#     if result == num1 * num2:
#         score += 20
#         print("맞았습니다.")
#     else:
#         print("틀렸습니다")
    
#다른 예시 확실히 더 좋은거같다. 많이 깔끔해짐
for _ in range(5):
    a =  random.randint(2,9)
    b =  random.randint(2,9)
    result = int(input(f'{a} * {b} = ')) #역시나 선언하는 구문이 있었다. {}
    if result == a * b:
        score += 20
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
        
#점수 등급 측정
#기초중에 기초인 if elif else
if score >= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"
print("최종 점수는", score, "점", grade, "입니다.")