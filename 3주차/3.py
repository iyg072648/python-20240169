#이중 for문 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{}={:2d}'.format(i,j, i*j), end = ' ')
    print()

#리스트,sum 값 합
nums = [10, 20, 30, 40, 50]
print('리스트 값의 합 :', sum(nums))

#1~100까지 합 sum,range 사용
print('1~100까지 합 :', sum(range(1,101)))

#순차적 구조 실행
num = 100
print('num =', num)
num  = num + 100
print('num =', num)
num  = num + 100
print('num =', num)

#if 조건문을 이용한 출력
num = 150
if num < 200:
    print('200')

#걸음수
walk_count = 1200
if walk_count >= 1000:
    print('목표 달성')

#피라미드 패턴
n = 5
for i in range(n):
    for j in range(n - (i + 1)):
        print(' ', end = '')
    for j in range(2 * i + 1):
        print('*', end = '')
    print()

#간결
n = 5
for i in range(n):
    print(' ' * (n - (i + 1)), end = '')
    print('+' * (2  * i + 1))