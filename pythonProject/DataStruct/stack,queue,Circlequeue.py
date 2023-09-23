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