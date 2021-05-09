# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

import sys

num = int(sys.stdin.readline().rstrip())
result = 0

for i in range(num + 1):
    if result >= num:
        print(i - 1)
        break
    result += i