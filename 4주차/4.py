# a = 1024
# a >> 1
# a >> 2

# a = a >> 1
# a

# a = a >> 1
# a

# a = 1
# a << 1

# a = a << 1
# a

# name = input("이름을 입력하세요 : ")
# print("이름 : ", name)
# age = int(input("나이를 입력하세요 : "))
# print("10년 후 나이 : ", age + 10)


# time = 8
# if time < 12:
#     print("오전")

# time = 13
# if time >= 12:
#     print("오후") 

# time = int(input("지금은 몇시입니까? : "))
# if time < 12:
#     print("지금은 오전", time, "시 입니다.")
# elif time >= 12:
#     print("지금은 오후", time, "시 입니다.")

# walk_count = int(input("걸음수를 입력하세요 : "))
# if walk_count >= 1000:
#     print("걸음수 목표달성")

num = int(input('정수를 입력하세요 : '))
print('n = ', num)
if num < 0:
    print(num, '은(는) 음수입니다')
else:
    print(num, '은(는) 음수가 아닙니다.')
    
    if num % 2 == 0:
        print(num, '은(는) 짝수입니다.')
    else:
        print(num, '은(는) 홀수입니다.')