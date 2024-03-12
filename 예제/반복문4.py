#for,range를 사용한 데이터 출력
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])
 
#len을 사용한 코드
for i in range(len(price_list)):
    print(price_list[i])

#data, enumerate사용
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)

#3,2,1 순으로 출력
for i in range(len(price_list)):
    print(3 - i, price_list[i])

#3이라는 숫자보단 일반적인 형태로 하는것이 좋음
for i in range(len(price_list)):
    print((len(price_list) - 1) -i, price_list[i])

#100,110,120 순으로 출력
for i in range(1,4):
    print(90 + 10 * i, price_list[i])

