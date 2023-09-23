line = input()

bracket = []

for j in line:
    if j == "(":
        bracket.append(j)
    elif j == ")":
        if len(bracket) != 0 and bracket[-1] == "(":
            bracket.pop()
        else:
            bracket.append(")")
            break

if len(bracket) == 0:
    print("YES")
else:
    print("NO")