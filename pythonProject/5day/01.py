#학생들의 수학, 영어 점수를 입력받아 이를 모아둔 점수표를 출력하세요.

# 학생 수 입력
n = int(input('Number of Students: '))

score = {}

for i in range(n):
    name = input('Name: ')
    math = int(input('Math: '))
    english = int(input('English: '))

    # score에 넣어봅시다.
    score[name]=[math, english]

# 내림차순 정렬
# sorted 함수 사용 예시
# result = sorted(list.items(), reverse = False)
# reverse가 False이면 오름차순, True이면 내림차순으로 사용할 수 있습니다.

score=sorted(score.items(), reverse=True)

print('==========ScoreList==========')
print(score)