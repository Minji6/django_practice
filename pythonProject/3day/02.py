#아래와 같은 조건을 만족하는 약수의 갯수 반환 함수 num_divisor을 완성하세요.
#약수란 어떤 수로 정수가 나누어 떨어지는것을 대하여 이르는 말을 의미합니다.
#예를 들어, 6은 1,2,3,6으로 나누어 떨어지기 때문에 4개의 약수를 가집니다.
#매개변수: num(int)
#반환값: 약수의 갯수(int)


def num_divisor(num):
    num_div = 0;
    for i in range(1, num+1):
        if num%i == 0:
            num_div += 1
    return num_div
x = int(input())
print(num_divisor(x))