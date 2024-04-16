# for i in range(5):
#     print((i+1) * "*")

# for i in range(5, 0, -1):
#     print("*" * i)

# for i in range(5):
#     for j in range(4-i):
#         print(" ", end ="")
#     for j in range(2*(i+1)-1):
#         print("*", end="")
#     print()

# for i in range(5, 0, -1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*", end="")
#     print()

# a = 9
# b = 3
# print (9 // 3)

# num = 200
# num += 100
# print(num)

# num -=100
# print(num)

# num *= 20
# print(num)

# num /= 2
# print(num)

# a, b = 100, 200
# print(a == b)

# print(a != b)

# print(a > b)

# print(a < b)

# print(a >= b)

# print(a <= b)

#문자열을 list화
# st = 'hello'
# list(st)
# print(list(st))

# for ch in 'hello':
#     print(ch, end=' ')

# #리스트 합
# nums = [1, 2, 3, 4, 5]
# s = 0

# #특정값 인덱스 찾기3
# f = ['apple', 'banana', 'cherry', 'banana', 'apple']
# t = 'apple'
# for num in nums:
#     s += num
# print(s)

# name = input("이름을 입력하세요 : ")
# zl = int(input("키를 입력하세요 (단위 cm) : "))
# if zl > 140:
#     print(name, "님은 놀이기구를 탈 수 있습니다.")
# else:
#     print(name, "님은 놀이기구를 탈 수 없습니다.")

# age = int(input("나이를 입력하세요 : "))
# zl = int(input("키를 입력하세요 (단위 cm) : "))
# if age > 19 :
#     if zl > 150:
#         print("입잘할 수 있습니다.")
#     else:
#         print("입장할 수 없습니다 (키)")
# else:
#     print("입장할 수 없습니다 (나이)")

# age = int(input("나이를 입력하세요 : "))
# if age >= 20:
#     print("Adult")
# elif age >= 10 and age < 20:
#     print("Youth")
# elif age < 10:
#     print("Kid")

# a, b = input("두 정수를 입력하세요 : ").split()
# a = int(a)
# b = int(b)
# print(a + b)

# a, b, c = map(int, input("숫자를 입력하세요 : ").split())
# m = [a, b, c]
# m.sort()
# print(m)

# for i in range(len(f)):
#     if f[i] == t:
#         print(f'{t} is at index {i}')

# #이중 for문 1~10 10번 반복
# for i in range(10):
#     for j in range(1, 11):
#         print(j, end=' ')
#     print()

#별찍기
# for i in range(1, 11):
#     for j in range(1, i+1):
#         print('*', end="")
#     print()

# for i in range(1, 11):
#     for j in range(10-i, 0, -1): #
#         print(' ', end="")
#     for j in range(1, i+1):
#         print('*', end='')
#     print()

# n = 5
# for i in range(n):
#     print(n - (i + 1), end=' ')

# n = 10
# for i in range(n):
#     print(2 * i + 2, end= ' ')

# for i in range(2, 10, 2):
#     print(i*2, end=' ')

# s = 0
# for i in range(1, 11):
#     s = s + i
# print('1에서 10까지의 합 :', s)

# s = 0
# for i in range(1, 11):
#     s += i
#     print('i = {}, s = {}'.format(i, s))
# print('1~10까지의 합 : ', s)

#혼동을 줄 가능성이 낮은 코드
# n = int(input("합계를 구할 수를 입력하세요 : "))
# s = 0

# for i in range(1, n+1):
#     s += i
# print('1~{}까지 합은 {}'.format(n, s))

#while문
# n = int(input("합계를 구할 양의 정수를 입력하세요 : "))
# s = 0 #결과값을 저장하는 변수
# i = 1 #제어변수

# while i <= n: #i는 1부터 시작해서 입력한 n값에 도달할때까지 반복
#     s = s + i
#     i += 1

# print('1부터 {}까지 합은 {}'.format(n, s))

#sum을 이용한 1~100까지의 합
# print('1~100까지의 합 : ', sum(range(1, 101)))

#소수 구하기
# n = int(input("수를 입력하세요 : "))
# is_prime = True
# for num in range(2, n):  #2부터 (n-1) 사이의 수 num에 대하여
#     if n % num == 0:     #이 수 중에서 n의 약수가 있다면
#         is_prime = False #소수가 아님

# print(n, 'is prime :', is_prime)

#소수를 담을 리스트 초기화
#2~100까지의 소수구하기
# primes = []

# for n in range(2, 101):
#     #일단 n을 소수로 둠
#     is_prime = True
#     for num in range(2, n):
#         if n % num == 0:
#             is_prime = False
#     if is_prime:
#         primes.append(n)

# print(primes)

#가위 바위 보 선택
# selected = None
# while selected not in ['가위', '바위', '보']: #리스트를 쓸 수 있다.
#     selected = input('가위, 바위, 보 중에서 선택하세요 > ')
# print('선택한 값은 :', selected)

#양수가 입력될때까지 반복하는 while문 (1~n까지 합)
# n = -1
# while n <= 0: #양수가 입력될 때 까지 input() 문을 반복함
#     n = int(input('합계를 구할 양의 정수를 입력하세요 : '))

# s = 0

# for i in range(1, n+1):
#     s += i

# print('1~{}까지의합은 {}'.format(n, s))

# st = 'difficulty'

#모음이 나타나면 즉시 반복문 종료하는 기능
# for ch in st:
#     if ch in ['a', 'e', 'i', 'o', 'u']:
#         break
#     print(ch)
# print('end')

#continue를 사용해서 모음일 경우 출력
# for ch in st:
#     if ch in ['a', 'e', 'i', 'o', 'u']:
#         continue
#     print(ch)
# print('end')
