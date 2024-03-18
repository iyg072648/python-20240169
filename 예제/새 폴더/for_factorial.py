#for 반복문을 이용한 팩토리얼(계승) 계산
n = int(input('수를 입력하세요 : '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print('{}! = {}'.format(n, fact))