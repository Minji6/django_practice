#점수 변환기
#한 과목에서 학생들의 최종 점수가 나왔습니다. 교수님은 이 점수를 가지고 학생들에게 학점 A, B, C, D, F 중 하나를 부여합니다.
#A: 80점 이상
#B: 60점 이상 80점 미만
#C: 40점 이상 60점 미만
#D: 20점 이상 40점 미만
#F: 20점 미만

#내 풀이
x = int(input())

if x >= 80:
    print('A')
elif x >= 60:
    print('B')
elif x >= 40:
    print('C')
elif x >= 20:
    print('C')
else:
    print('F')

#우수 답안

score = int(input(x))

if score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 40:
    grade = 'C'
elif score >= 20:
    grade = 'D'
else:
    grade = 'F'
print(grade)


