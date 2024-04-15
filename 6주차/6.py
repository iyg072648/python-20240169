# for i in range(2, 10):
#     for j in range(1, 10):
#         print('{}*{} = {:2d}'.format(i, j, i*j), end=' ')
#     print()

# n = 7
# for i in range(n):
#     st = ''
#     for j in range(i):
#         st = st + ' '
#     print(st +'#')

# n = 7
# for i in range(n):
#     print(' '*i+'#')

# n = 7
# for i in range(6, -1, -1):
#     st = ''
#     for j in range(i):
#         st = st + ' '
#     print(st +'#')

# n = int(input("합계를 구할 양의 정수를 입력하세요 : "))
# s = 0 #결과값을 저장하는 변수
# i = 1 #제어변수

# while i <= n: #i는 1부터 시작해서 입력한 n값에 도달할때까지 반복
#     s = s + i
#     i += 1

# print('1부터 {}까지 합은 {}'.format(n, s))