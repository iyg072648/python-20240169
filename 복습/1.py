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

# #리스트 합
# nums = [1, 2, 3, 4, 5]
# s = 0

# for num in nums:
#     s += num
# print(s)

# #특정값 인덱스 찾기3
# f = ['apple', 'banana', 'cherry', 'banana', 'apple']
# t = 'apple'

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
#     print()2