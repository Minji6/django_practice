# 기본 코드입니다. 수정하시면 안됩니다.
medals = [ ( 'Australia', 2, 1, 0 ),
           ( 'Austria', 4, 6, 6 ),
           ( 'Belarus', 1, 1, 1 ),
           ( 'Canada', 14, 7, 5 ),
           ( 'China', 5, 2, 4 ),
           ( 'Croatia', 0, 2, 1 ),
           ( 'Czech Republic', 2, 0, 4 ),
           ( 'Estonia', 0, 1, 0 ),
           ( 'Finland', 0, 1, 4 ),
           ( 'France', 2, 3, 6 ),
           ( 'Germany', 10, 13, 7 ),
           ( 'Great Britain', 1, 0, 0 ),
           ( 'Italy', 1, 1, 3 ),
           ( 'Japan', 0, 3, 2 ),
           ( 'Kazakhstan', 0, 1, 0 ),
           ( 'Korea', 6, 6, 2 ),
           ( 'Latvia', 0, 2, 0 ),
           ( 'Netherlands', 4, 1, 3 ),
           ( 'Norway', 9, 8, 6 ),
           ( 'Poland', 1, 3, 2 ),
           ( 'Russian Federation', 3, 5, 7 ),
           ( 'Slovakia', 1, 1, 1 ),
           ( 'Slovenia', 0, 2, 1 ),
           ( 'Sweden', 5, 2, 4 ),
           ( 'Switzerland', 6, 0, 3 ),
           ( 'United States', 9, 15, 13 ) ]


country_name = input() # 순위를 찾고싶은 국가의 이름을 입력합니다. 위에 있는 국가의 이름만 입력된다고 가정합니다.

# 여기에 코드를 짜주세요.
for i in range(len(medals)):
    con, gold, silver, bronze = medals[i]
    medals[i] = gold, silver, bronze, con

medals.sort(reverse = True)

for i in range(len(medals)):
    if country_name == medals[i][3]:
        print(i+1)



