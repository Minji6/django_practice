#for을 이용하여 [76점, 59점, 95점, 87점, 61점] 채점 결과의 총합과 평균을 구하여라.

x = [76,59,95,87,61]
y=0

for i in range(len(x)):
    y += x[i]
print(y)
print(y/len(x))
