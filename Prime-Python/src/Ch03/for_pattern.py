# 코드 3-38 : for 루프와 *를 사용한 패턴 생성하기
## "으뜸 파이썬", p. 166

n = 7
for i in range(n): # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
    print (' ' * i + '#')  # 공백을 i번 추가한 후 '#'출력
