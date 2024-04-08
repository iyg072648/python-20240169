# num1 = int(input("첫번째 숫자를 입력하세요 : "))
# num2 = int(input("두번째 숫자를 입력하세요 : "))

# if (num1 % 2 == 0) and (num2 % 2 == 0):
#     print('두 수 모두 짝수입니다')

# if (num1 % 2 == 0) or (num2 % 2 == 0):
#     print('두 수 중 하나 이상이 짝수입니다.')

# else:
#     print('두 수 모두 홀 수 입니다.')

# score = int(input('점수를 입력하세요 : '))

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# print('당신의 등급은 : ', grade)

# speed = int(input('자동차의 속도를 입력하세요 : '))

# if speed >= 100:
#     s = '고속'
# elif speed < 100 and speed >= 60:
#     s = '중속'
# else:
#     s = '저속'

# print(s)

# s = 0
# for i in range (1, 101):
#     s = s + i
# print('1~100까지의 합 : ', s)

n = int(input('합계를 구할 수를 입력하세요 : '))
s = 0

for i in range(1, n + 1):
    s = s + i
print('1부터 {}까지의 합은 : '.format(n, s))