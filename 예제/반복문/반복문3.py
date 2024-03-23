#for,range로 0~99까지 출력
for i in range(100):
    print(i)

#range를 사용해서 2002~2050년까지 개최년도 출력
for x in range (2002, 2051, 4):
    print(x)


#1~30까지 3의 배수 출력
for num in range(3, 31, 3):
    print(num)

#99부터 0까지 1씩 감소하는 숫자들을 출력
for i in range(100):
    print(99 - i)

#for문을 사용해서 0.1씩 증가
for num in range(10):
    print(num/10)

#구구단 3단 출력
for i in range(1, 10):
    print(3, "x", i, "=", 3 * i)

#홀수출력
num = 3
for i in range (1, 10):
    if i % 2 == 1: #나눠서 1이 남는 숫자일때
        print(num, "x", i, "=", num * i)

#1~10까지 더한 수
hab = 0
for i in range(1, 11):
    hab += i
print ("합 :", hab)

#모든 홀수를 합해서 출력
hab = 0
for i in range(1, 11, 2):
    hab += i
print ("합 :", hab)

#1~10까지 곱한 수 출력
result = 1
for i in range(1, 11):
    result *= i
    #result = result * i 축약하여 작성한 코드
print(result)