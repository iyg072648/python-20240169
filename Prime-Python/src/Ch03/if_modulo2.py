# 코드 3-7 : 3과 5의 배수를 판단하기 위한 모듈로 연산과 and 조건문
## "으뜸 파이썬", p. 126

number = int(input('정수를 입력하세요 : '))

if (number % 3) == 0 and (number % 5) == 0:
    print(number, '은(는) 3의 배수이면서 5의 배수입니다.')
