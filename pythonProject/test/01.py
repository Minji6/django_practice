#수열 출력하기 응용
fruit = ['귤', '사과', '복숭아']

for x in range(int(input())):
    print(fruit[x%3], end="")