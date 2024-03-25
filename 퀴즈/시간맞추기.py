import time as t

input("5초 맞추기 게임 시작! 엔터 키를 눌러주세요.")
start_time = t.time()

input("5초를 맞춰주세요! 엔터 키를 눌러주세요.")
end_time = t.time()

# print(end_time - start_time)
check_time = end_time - start_time

if 4.5 <= check_time < 5.5: 
#if 4.5 <= check_time and check_time <= 5.5: C 또는 자바에서는 수정
    print(check_time, ": 축하합니다.")
elif check_time < 4.5:
    print(check_time, ": 너무 빨라요!")
else:
    print(check_time, ": 너무 느려요!")
