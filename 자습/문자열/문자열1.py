#문자열 인덱싱
#두번째자리까지 인덱싱.
lang = 'python'
print(lang[0], lang[2])

#[::] 시작인덱스:끝인덱스:오프셋
string  = "홀짝홀짝홀짝"
print(string[::2])

#문자열 슬라이싱

#[int:]는 음수값은 문자열 뒤
license_plate = "24가 2210"
print(license_plate[-4:])

#오프셋이 음수일경우 문자열 끝부터 정렬
string = "PYTHON"
print(string[::-1])

#문자열 치환

#.replace로 -하이푼을 공백으로 바꾼다. 공백이 아닌 다른 것으로도 변경가능하다
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

#'.' 기준으로 분리하고 분리된 url중 마지막을 인덱싱하여 도메인을 출력
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

#문자열은 immutable

#문자열은 수정 불가. 메서드 지원 하지않음.
# lang = 'python'
# lang[0] = 'P'
# print(lang)
#replace 메서드

string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

#문자열 변경할수없는 자료형
#replace 메서드를 사용해서 원본은 그대로 둔채로
#새로운 문자열 객체로 리턴
string = 'abcd'
string.replace('b', 'B') # 변경할려면 string=string.replace 사용
print(string)