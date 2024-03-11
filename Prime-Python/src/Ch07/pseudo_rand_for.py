# 코드 7-7 : 의사 랜덤 함수를 이용한 연속적인 난수 만들기
## "으뜸 파이썬", p. 410

def pseudo_rand(x):
    new_x = (1103515245 * x + 12345) % ( 2 ** 31 )
    return new_x

x = 45         # 씨앗(seed)되는 초기 번호
for _ in range(15):
    x = pseudo_rand(x)
    print(x)
