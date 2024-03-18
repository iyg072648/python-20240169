#2~9까지 구구단

for i in range (2, 10): #외부 for 루프 2~9까지
    for j in range(1, 10): #내부 for 루프
        print('{}*{}= {:2d}'.format(i, j, i*j), end = '  ') 
    print() #내부 루프 수행 후 줄바꿈을 함