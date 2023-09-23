#올림픽 메달 숫자 세기 수업시간에 나온 올림픽 메달 예제를 이용해 미션을 수행해보세요.
#입력 숫자를 받아 그 숫자보다 많은 금메달, 은메달, 동메달을 딴 국가를 출력하세요. (이상이 아니라 초과입니다)
#예를 들어, 입력된 숫자가 4 일때, 금메달, 은메달, 동메달을 각각 모두 5개 이상 딴 국가를 모두 출력해야 합니다. United States가 그 중 한 예입니다.
#출력할 때는 아래와 같이 리스트를 print()로 출력해야 합니다.

# 기본 코드입니다. 수정하시면 안됩니다.
countries = [ "Australia", "Austria", "Belarus", "Canada",
              "China", "Croatia", "Czech Republic", "Estonia",
              "Finland", "France", "Germany", "Great Britain",
              "Italy", "Japan", "Kazakhstan", "Korea", "Latvia",
              "Netherlands", "Norway", "Poland", "Russian Federation",
              "Slovakia", "Slovenia", "Sweden", "Switzerland",
              "United States" ]

gold = [2, 4, 1, 14, 5, 0, 2, 0, 0, 2, 10, 1, 1,
        0, 0, 6, 0, 4, 9, 1, 3, 1, 0, 5, 6, 9]

silver = [1, 6, 1, 7, 2, 2, 0, 1, 1, 3, 13, 0, 1, 3, 1,
          6, 2, 1, 8, 3, 5, 1, 2, 2, 0, 15]

bronze = [0, 6, 1, 5, 4, 1, 4, 0, 4, 6, 7, 0, 3, 2, 0,
          2, 0, 3, 6, 2, 7, 1, 1, 4, 3, 13]

# 아래 코드부터 수정해주세요.
num = int(input())
ans = []

for i in range(len(countries)):
    if (gold[i] > num) & (silver[i] > num) & (bronze[i] > num):
        ans.append(countries[i])

ans.sort() #sort()함수는 ans를 오름차순 정렬합니다.
print(ans)