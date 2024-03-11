print("hello python!")
print("my name is inyeong")

# for i in range (2, 10): #외부 for 루프 2~9까지
#     for j in range(1, 10): #내부 for 루프
#         print('{}*{}= {:2d}'.format(i, j, i*j), end = '  ') 
#     print() #내부 루프 수행 후 줄바꿈을 함

# a = int(input('a를 입력하세요 : '))
# b = int(input('b를 입력하세요 : '))
# c = a + b
# print ('a 와 b의 합은 : ', a + b)
# if c % 3 == 0:
# 	print(c, '는 3의 배수입니다')
# else:
# 	print(c, '는 x')

년 = int(input('출생년도를 입력하세요 : '))
월 = int(input('월을 입력하세요 : '))
일 = int(input('일을 입력하세요 : '))
print('당신의 생년월일은 ', 년, '년', 월, '월', 일, '일 입니다')