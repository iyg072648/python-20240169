#정수를 제외한 음수만 츨력

리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0: #변수가 0보다 작을때 변수에 저장
        print(변수)

#for문을 사용해서 배수 출력
        
리스트  = [3, 100, 23, 44]
for 변수 in 리스트:
    if 변수 % 3 == 0: #3으로 나누었을때 0이되는면 변수에 저장
        print(변수)

#리스트에서 n수보다 작은 수들중에서 배수를 출력
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
        if(변수 < 20) and (변수 % 3 == 0): #20보다 작고 3의 배수인 숫자
             print(변수)

#리스트에서 세글자 이상의 문자만 출력
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
    if len(변수) >= 3: #글자가 3글자일경우 변수에 저장
         print(변수)

#대문자 출력
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
     if 변수.isupper():#isupper() 메서드는 대문자 여부 판별
          print(변수)

#False
for 변수 in 리스트:
    if 변수.isupper() != False:
         print(변수)          

#True
for 변수 in 리스트:
    if 변수.isupper() != True:
         print(변수)          

for 변수 in 리스트:
    if not 변수.isupper():#논리 연산자 not 사용
        print(변수)

#첫글자를 대문자로 변경
리스트 = ['dog', 'cat', 'parrot']

#인덱싱으로 첫글자를 가져오고
#upper함수로 대문자로 변경
#변경한 대문자와 나머지 문자를 이어붙인다.
for 변수 in 리스트:
    첫글자 = 변수[0]
    대문자 = 첫글자.upper()
    print(대문자 + 변수[1:])

#한줄코드
for 변수 in 리스트:
    print(변수[0].upper() + 변수[1:])

#확장자 제거

#split 메서드로 마침표를 구분자로 분열
#그리고 0번째 인덱스부터 파일이름 출력
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
    split = 변수.split(".")
    print(split[0])

#확장자 이름명 확인
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".") # .을 기준으로
    if split[1] == "h": #확장자가 h인지 비교
        print(변수)

#2가지 확장자 이름 확인
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(변수)
