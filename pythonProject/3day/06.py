#math 모듈을 사용하여 반지름 r을 입력받은 후 원의 넓이를 출력해주세요.

from math import pi

def pimath(r):
    return pi*(r**2)

r=int(input())
print(pimath(r))