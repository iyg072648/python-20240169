# 코드 10-18 : 문자열 각각을 대문자로 바꾸는 기능
## "으뜸 파이썬", p. 593

st = 'Hello World'
s_list = [x.upper() for x in st]  # 문자열 각각에 대해 upper() 메소드 적용
print(s_list)
