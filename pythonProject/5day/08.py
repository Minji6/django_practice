# 기본 코드입니다. 수정하지 마세요.
score = {"John": 89, "Jenny": 19, "Henry": 58, "Leia": 93, "Minsaku": 91, "Juho": 78, "Harry": 49, "Kim": 67,
         "Gabriel": 37}

threshold = int(input())
# 여기서부터 코딩해주시면 됩니다.
# print(score.items())

sorted_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
# print(sorted_score)

names = []

for name_score in sorted_score:
    if name_score[1] < threshold:
        break
    else:
        names.append(name_score[0])

names.sort()
print(names)


