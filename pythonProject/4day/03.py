#입력: 순서대로 10개의 미세먼지 농도를 입력받습니다.
#출력: 이를 오름차순 정렬한 후 출력하세요.

pollution = []
for i in range(10):
    pollution.append(int(input()))

sort_pollution = pollution
sort_pollution.sort()
print(sort_pollution)