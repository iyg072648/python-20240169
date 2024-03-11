#이중 for 루프를 사용한 패턴 생성하기

n = 7
for i in range(n): # 외부 for 루프는 n번 수행, i는 0~6까지 증가
    st = ' ' # st는 공백이라 침
    for j in range(i): # 내부 for 루프는 i번 수행
        st = st + ' ' # 공백을 i개 추가함
    print(st + '#') # 공백 추가 후 '#'출력

#n번의 일정한 패턴을 만들면서
#다음 줄으로 넘어갈때마다 공백 한칸씩 추가.