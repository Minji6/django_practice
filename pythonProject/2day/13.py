#수열 출력하기
#입력된 숫자만큼 숫자 1, 2, 3이 반복되는 규칙적인 수열을 출력해봅시다.

n = int(input())

for i in range(n):
    i = i%3+12
    print(i, end=" ")

