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

#0,1,2를 바인딩하고 인덱싱을 사용한 출력
my_list = ["가", "나", "다", "라"]
for i in [0, 1, 2]:
    print(my_list[i])

#행이 증가할때마다 인덱스 1씩 증가
my_list = ["가", "나", "다", "라", "마"]


# print(my_list[0], my_list[1], my_list[2])
# print(my_list[1], my_list[2], my_list[3])
# print(my_list[2], my_list[3], my_list[4])

#출력ㅎ고 싶은 값의 위치를 나열, i, i+1, i+2
for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1], my_list[i+2])

#다른 예시들
for i in range( len(my_list) - 2 ):
    print(my_list[i], my_list[i+1], my_list[i+2])
for i in range( 1, len(my_list) - 1 ):
    print(my_list[i-1], my_list[i], my_list[i+1])
for i in range( 2, len(my_list) ):
    print(my_list[i-2], my_list[i-1], my_list[i])

#반복문, range를 사용해서 역순 출력
my_list = ["가", "나", "다", "라"]

#인덱스가 1씩 감소
for i in [3, 2, 1]:
    print(my_list[i], my_list[i-1])

#일반적인 형태로 코드 수정
for i  in range(len(my_list) - 1, 0 , -1):
    print(my_list[i], my_list[i-1])

#4개의 정수를 각각 데이터에 자신의 우측값과 차분값을 출력
my_list = [100, 200, 400, 800]

#인덱스의 관계 파악후 기준으로 사용할 인덱스 결정
for i in [0, 1, 2]:
    print(abs(my_list[i+1] - my_list[i]))

#코드 정리
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

#6일간의 종가데이터를 3일 이동 평균 계산

my_list = [100, 200, 400, 800, 1000, 1300]

#관계 파악
for i in [1, 2, 3, 4]:
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1] / 3))

for i in range(1, len(my_list) - 1): #1 ~ -1까지 len(my_list)로 데이터를 불러온다
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1] / 3)) #불러온 데이터에 한해서 3일 이동 평균 계산.

#저가, 고가 정보의 변동폭을 low, high 2개의 리스트를 사용해서 5일간의 volatility 리스트에 변동폭 저장
    
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])