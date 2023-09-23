'''5! = 1 * 2 * 3 * 4 * 5
factorial을 재귀함수를 이용해 구해보세요!'''

# def factorial(n):
# TODO: 팩토리얼을 재귀함수를 이용해 구해보세요.
#    if n == 1:
#        return 1
#    else: return n * factorial(n-1)

# res = factorial(5)
# print(res)

# 반복문 for
import math

n = 1
for i in range(n):
    n * math.factorial(n - 1)
print()
