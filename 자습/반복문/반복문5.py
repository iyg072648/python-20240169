#하나의 행을 리스트로 3개의 리스트를 갖는 이차원 리스트
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]

#2개의 리스트를 갖는 이차원 리스트
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

#딕셔너리로 표현 시가,종가 키로 지정하고 데이터를 리스트로 저장해서 value로 저장
stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}

#날짜 딕셔너리
stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}

#아래 저장된 리스트를 한줄씩 출력
apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row: 
        print(col, "호")

#역순
for row in apart[::-1]:
    for col in row:
        print(col, "호")

#출력2
for row in apart:
    for col in row:
        print(col, "호")
        print('-' * 5)

#출력3
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")

#출력4
for row in apart:
    for col in row:
        print(col, "호")
print("-" * 5)