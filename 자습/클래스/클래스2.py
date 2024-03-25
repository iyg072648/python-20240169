#객체가 생성될때 입력받을수있는 생성자 정의
# 삼성 = Stock("삼성전자", "005930")

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

#메서드 추가
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    #리턴하는 메서드
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

a = Stock(None, None)
a.set_name("삼성전자") # Stock.set_name(a, "삼성전자")
a.set_code("005930")
print(a.name)
print(a.code)

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name())
print(삼성.get_code())

class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
    
#객체 생성
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.배당수익률)


#객체의 속성 수정
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

#per 호출후 값 수정
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)

#여러 객체의 생성
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문