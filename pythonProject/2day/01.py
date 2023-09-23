#input을 이용하여 자연수를 입력 받고 if, elif, else를 이용하여 주어진 자연수가 홀수인지 짝수인지 판단하여라

x = int(input("Enter the integer: "))
y=x%2

if y == 0:
    print('even number')
else: print('odd number')