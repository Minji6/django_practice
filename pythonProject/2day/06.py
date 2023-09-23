#시작 값과 끝 값을 입력받아
#시작 값 이상 끝 값 미만에 있는 모든 짝수를 차례로 출력하는 코드를 작성하세요.
#한 space 씩 뛰어서 출력하기 위해 print(…, end=’ ‘)를 활용하세요.

first = int(input())
end = int(input())

for i in range(first,end):
    if i % 2 == 0:
        print(i, end=' ')