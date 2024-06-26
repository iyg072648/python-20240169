# 코드 4-9 : 2차 방정식의 근을 구하는 기능의 반복 사용
## "으뜸 파이썬", p. 209

a = 1
b = 2
c = -8
# 근의 공식으로 해를 한 번 더 구한다.(반복되는 코드)
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는', r1, '또는', r2)

a = 2
b = -6
c = -8
# 근의 공식으로 해를 한 번 더 구한다.(반복되는 코드)
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는', r1, '또는', r2)
