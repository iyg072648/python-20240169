# 코드 3-29 : for 반복문을 이용한 5 팩토리얼(5!) 계산
## "으뜸 파이썬", p. 158

n = int(input('수를 입력하세요 : '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print('{}! = {}'.format(n, fact))
