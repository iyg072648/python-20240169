import random

score = 0

#num1,num2에 randrange로 변수 선언
num1 = (random.randrange(1,10))
num2 = (random.randrange(1,10))

#출력값 확인
print(num1)
print(num2)

print(num1, '*', num2, '=') #어쩔수없이 print,input 따로따로 출력
result = int(input()) #선언 어떻게하지;;;
if result == num1 * num2:
    score += 20
    print("맞았습니다.")
else:
    print("틀렸습니다")

#일단 작동은 잘되나 되게 비효율적
#아직 구문 모르는게 많으니 패스.
    