#문자열 합치기

#정수가 아닌 문자열로 나열해서 그대로 합쳐진다.
a = "3"
b = "4"
print(a+b)

#문자열의 곱셈은 반복을 의미한다.
print("HI" * 3)

#- 80개 반복
print('-' * 80)

#문자열 곱하기

t1 = 'python'
t2 = 'java'
print((t1 + t2) * 4)


#정답
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

#문자열 출력

#print 포맷팅에서는`%s`는 문자열 데이터 타입의 값을 
#`%d`는 정수형 데이터 타입 값의 출력을 의미
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))


#윗 문제를 format() 메서드를 이용해서 다시 풀기
#%s,%d자리에 {} 적어주고 .format으로 풀어준다.

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : {} 나이 : {}".format(name1, age1))

#f-string

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#컴마 제거하기

#int를 사용하면 되지만 먼저 replace로 컴마를 제거후 사용
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

#문자열 슬라이싱

#문자열에서 슬라이싱을 사용하면 여러글자를 접근할 수 있다.
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#strip 메서드
#좌우 공백을 제거, 문자열은 그대로 유지되며
#새로운 문자열이 반환된다.
data = "   삼성전자    "
data1 = data.strip()
print(data1)