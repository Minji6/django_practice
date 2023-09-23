#사용자에게 input을 사용하여 3개의 값을 받습니다. (각각 r,g,b)를 나타내는 수치들 입니다.
#color_complementary(r,g,b) 함수를 작성합니다.
#color_complementary(r,g,b) 함수를 호출하여 보색변환 이후의 r,g,b값을 comma로 구분된 괄호의 형태로 출력합니다.

def color_complementary(r,g,b):
    return 255-r, 255-g, 255-b

a=int(input())
b=int(input())
c=int(input())

a,b,c=color_complementary(a,b,c)
print('(',a,',',b,',',c,')')