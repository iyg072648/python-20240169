# #비어있는 Human 클래스 정의
# class Human:
#     pass

# #이름 지정 바인딩
# inyeong = Human()

# class Human:
#     def __init__(self):
#         print("휴먼")

# inyeong = Human()

#클래스 생성자
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

inyeong = Human("인영", 25)
print(inyeong.name)
print(inyeong.age)

#클래스 메소드
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who(self):
        print("이름: {} 나이: {}".format(self.name, self.age))

    def setInfo(self, name, age):
        self.name = name
        self.age = age

    # def __del__(self):
    #     print("죽음")

inyeong = Human("불명", "미상")
inyeong.who()
    
inyeong.setInfo("인영", 25)
inyeong.who() #Human.who(inyeong)

# del(inyeong)