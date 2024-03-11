# 코드 8-19 : try-except 문을 사용한 파일 입출력
## "으뜸 파이썬", p. 502

import sys

fname = input('입력할 파일의 이름 : ')
try :
    f = open(fname, 'r', encoding = 'UTF8')  # 파일 열기
except IOError:
    print('Could not read file:', fname)
    sys.exit()
except:
    print('Unexpected error:', sys.exc_info()[0])
    sys.exit()

n = 1               # n을 1로 초기화 함
l = f.readline()    # 변수 l은 읽어들인 한 줄의 문자열을 저장합니다.
while l :
    print('{:3d}: {}'.format(n, l), end = '')
    n += 1          # 한 줄을 출력한 후 줄 수를 증가시킨다
    l = f.readline()# 다음 줄을 읽어온다
f.close()
