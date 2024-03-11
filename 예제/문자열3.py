#upper 메서드
#대문자로 변경된 새로운 문자열 객체가 반환
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#소문자로 변경된 새로운 문자열 객체가 반환
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

#capitalize 메서드
#맨 첫글자를 대문자로 반환?...
a = "hello"
a = a.capitalize()
print(a)

#endswith 메서드
#파일 이름이 xlsx 또는 xls로 끝나는지 확인
file_name = "보고서.xlsx"
file_name.endswith("xlsx","xls")

#startswith 메서드
#파일 이름 시작이 2020으로 시작하는지 확인
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

#split 메서드
#문자열 공백 기준으로 분리.
a = "hello world"
a.split()
#문자열 분리 ex) _
ticker = "btc_krw"
ticker.split("_")

#날짜를 표하는 문자열이 있을때
date = "2020-05-01"
date.split("-")

#rstrip 메서드
#공백이 제거된 새로운 문자열 객체 반환
#다만 기존 공백이 포함된 문자열은 메모리에서 삭제.
data = "039490     "
data = data.rstrip()