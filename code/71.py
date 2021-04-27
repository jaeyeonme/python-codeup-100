# 임의의 정수가 줄을 바꿔 계속 입력된다.
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

# 예시
# ...
# n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
# while n!=0 :
#   n = int(input())
#   if n!=0 :
#     print(n)
# ...

# 참고
# if 조건식 :
#   ...
#   ...


# 구조를 사용하면,
# 주어진 조건식의 평가 결과가 True 인 경우에만, 들여쓰기로 구분된 코드블록이 실행된다.

# if 를 while 로 바꾸면?

# while 조건식 :
#   ...
#   ...

# 와 같은 방법으로 반복해서 실행시킬 수 있다.

# 실행되는 과정은
# 1. 조건식을 평가한다.
# 2. True 인 경우 코드블록을 실행한다.
# 3. 다시 조건식을 평가한다.
# 4. True 인 경우 코드블록을 실행한다.
# ...
# ... 조건식의 평가 값이 False 인 경우 반복을 중단하고, 그 다음 명령을 실행한다.

# 조건식의 평가 결과가 True 동안만 반복 실행된다.

# 반복실행구조 안에 다른 조건/선택실행구조를 넣을 수도 있고...
# 조건/선택실행구조 안에 다른 반복실행구조를 넣을 수도 있다.

import sys

while True:
    num = int(sys.stdin.readline())

    if num is 0:
        break
    print(num)
