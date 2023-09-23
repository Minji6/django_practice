### 실습 1 피보나치 수열
# O(2^n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


### 실습 2 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


### 실습 3 문자열 길이 출력
def length(s):
    if s == "":
        return 0
    else:
        result = length(s[1:])
        return 1 + result


### 실습 4 문자열 거꾸로 출력
def reverse(s):
    if s == "":
        return
    else:
        reverse(s[1:])
        print(s[0], end='')