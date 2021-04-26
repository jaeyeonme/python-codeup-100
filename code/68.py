# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# 예시
# ...
# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#    print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D')
# ...

# 참고
# 여러 조건들을 순서대로 비교하면서 처리하기 위해서 조건문을 여러 번 중첩할 수 있다.

# if 조건식1 :
#   ...
# else :
#   if 조건식2 :
#     ...
#   else :
#     if 조건식3 :
#       ...
#     else :
#       ...
# ...
# 와 같이 조건/선택 실행 구조를 겹쳐 작성하면 순서대로 조건을 검사할 수 있다.
# 어떤 조건이 참이면 그 부분의 내용을 실행하고 전체 조건/선택 구조를 빠져나가게 된다.

# if 조건식1 :
#   ...
# elif 조건식2 :
#   ...
# elif 조건식3 :
#   ...
# else :
#   ...
# 도 똑같은 기능을 한다. elif는 else if 의 짧은 약어라고 생각해도 된다.
# elif 를 사용하면 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러 번 안 쪽으로 들여쓰기 하지 않아도 된다.

import sys

nums = int(sys.stdin.readline())

if nums >= 90 and nums <= 100:
    print('A')
elif nums >= 70 and nums <= 89:
    print('B')
elif nums >= 40 and nums <= 69:
    print('C')
else:
    print('D')
