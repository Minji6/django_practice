### () [] 다 포함.
line = input()

bracket = []

for j in line:
    if j == '[' or j == '(' :
        bracket.append(j)
    elif j == ']' :
        if len(bracket) != 0 and bracket[-1] == '[' :
            bracket.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
        else :
            bracket.append(']')
            break
    elif j == ')' :
        if len(bracket) != 0 and bracket[-1] == '(' :
            bracket.pop()
        else :
            bracket.append(')')
            break

if len(bracket) == 0:
    print("YES")
else:
    print("NO")