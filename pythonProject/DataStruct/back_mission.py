'''후위 표기법은 연산자 우선순위를 고려해 컴퓨터가 연산을 수행할 수 있도록, 연산자의 위치를 두 피연산자의 뒤에 표시하는 표현법입니다.

예제

3 + 5 # 중위 표기법
3 5 + # 후위 표기법
Copy
3 + 10 / 2 + 9 - 4 # 전위
3 10 2 / + 9 + 4 - # 후위
Copy

후위 표기법으로 입력된 수식을 계산해주는 계산기를 만들어주세요.

결과값을 print()로 출력합니다.
결과값에 반드시 int()를 씌워주세요.

print(int(res))
Copy
수식은 공백으로 구분되며, (, ) 등의 괄호는 포함하지 않습니다. 입력되는 수는 모두 양수 입니다. 음수(ex: -3)나 소수(ex: 0.3)를 포함하지 않습니다.

입력 예시

3 4 +
Copy
출력 예시

7
Copy
Hint
string.isdigit()은 문자열이 순수한 숫자 (-, . 등을 미포함)이면 True를 return 합니다.'''


class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return not self.arr

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        return self.arr.pop()

    def top(self):
        return self.arr[-1]


stack = Stack()
for i in range(5):
    stack.push(i)
    print("push: ", i)

print(stack.is_empty())
while not stack.is_empty():
    print("pop: ", stack.pop())

prev = Stack()
next = Stack()
curr_site = "home"
while True:
    print()
    print("현재 사이트는", curr_site, "입니다.")
    page = input("action: ")

    if page == "exit":
        break
    elif page == "-1":
        if not prev.is_empty():
            next.push(curr_site)
            print("top: ", prev.top())
            curr_site = prev.pop()
            print("curr 변경: ", curr_site)
        else:
            print('뒤로 갈 수 없습니다.')
    elif page == "1":
        if not next.is_empty():
            prev.push(curr_site)
            curr_site = next.pop()
        else:
            print('앞으로 갈 수 없습니다.')
    else:
        prev.push(curr_site)
        curr_site = page
        while not next.is_empty():
            next.pop()