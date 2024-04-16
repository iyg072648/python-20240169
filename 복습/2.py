# #한줄씩 넘어갈때마다 *추가
# #정방향 계단식
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end='')
#     for j in range(1, i+1):
#         print(end='')
#     print()

# #역방향 계단식
# for i in range(1, 6):
#     for j in range(6-i-1):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()

# #5부터 1까지 1씩 작아지게 5줄
# #별 개수도 i와 동일
# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

# #역방향
# for i in range(5, 0, -1):
#     for j in range(5-i):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()

# #피라미드
# for i in range(5):
#     for j in range(4-i):
#         print(' ', end="")
#     for j in range(2*(i+1)-1):
#         print('*', end='')
#     print()

# n = 7
# for i in range(n):
#     print(' ' * i + '#')

# for i in range(5, 0, -1):
#     for j in range(1, 6):
#         if j == i:
#             print('#', end="")
#         else:
#             print(' ', end='')
#     print()

# for i in range(4):
#     print("---------")

# 리스트 = ["김밥", "라면", "튀김"]
# for 메뉴 in 리스트:
#     print("오늘의 메뉴 :", 메뉴)

#글자수
# 리스트 = ['dog', 'cat', 'parrot']

# for 동물 in 리스트:
#     print(동물, len(동물))

#i값에 따라 *도 같이 추가됨
# for i in range(5):
#     print((i+1) * "*")

#5부터 0까지 -1칸씩
#*에 i를 곱하여 출력
# for i in range(5, 0, -1):
#     print('*'*i)

#별 역방향
# for i in range(5, 0, -1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# students = [75, 80, 93]

# num = 0
# for student in students:
#     num += 1
#     if student < 80:
#         continue
#     print("%d번 학생 합격입니다." %num)

    # if student >= 80:
    #     print('%d번 학생은 합격입니다.' %num)
    # else:
    #     print('%d번 학생은 불합격입니다.' %num)

# sum = 0
# for i in range(1, 10):
#     sum += i
# print(sum)

# a = [1, 2, 3]
# box = []
# for num in a:
#     box.append(num*10)
# print(box)

# x = int(input("숫자를 입력하세요 : "))
# if x != 10:
#     print("ok")

# num = int(input("정수를 입력하세요 : "))
# if (num % 5) == 0 and (num % 10) == 0:
#     print(num, "은(는) 5의 배수이면서 10의 배수입니다.")

# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{}*{} = {:2d}".format(i, j, i*j), end=' ')
#     print()


# for i in range(5):
#     for j in range(4-i):
#         print(' ', end='')
#     for j in range(2*(i+1)-1):
#         print('*', end='')
#     print()