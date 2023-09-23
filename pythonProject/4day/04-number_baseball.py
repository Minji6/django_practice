#‘숫자 야구게임’의 점수를 계산하여 봅시다.
'''규칙은 아래와 같습니다.
사용되는 숫자는 0에서 9까지 중 세개로 서로 다른 숫자이다.
숫자는 맞지만 위치가 틀렸을 때는 볼.
숫자와 위치가 전부 맞으면 스트라이크.
해당 라운드의 점수는 볼의 수 * 1점 + 스트라이크의 수 * 3점으로 계산합니다.

예를 들어, 정답이 “012”이고, 해당 라운드에 “031”을 제시하였다면 1스트라이크, 1볼이되어 4점을 얻게 됩니다.
맨 처음에는 정답 숫자를 입력 받습니다.
두 번째 줄부터 여섯 번째 줄까지는 총 5번의 라운드 예상 숫자를 제시하게 됩니다.
매 라운드 점수의 총합을 결과로 출력하게 됩니다.
주의사항: 0이 맨 첫자리에 나올 수 있어 int 타입의 사용에 유의해야 합니다.'''


def number_baseball(correct_value, predict_value):
    # 정답과 예측값의 숫자 야구 점수를 계산하는 함수를 작성해 봅시다.
    correct_list = []
    predict_list = []
    ret = 0

    for i in range(3):
        correct_list.append(correct_value % 10)
        correct_value //= 10
        predict_list.append(predict_value % 10)
        predict_value //= 10

    for correct_idx in range(3):
        for predict_idx in range(3):
            if correct_list[correct_idx] == predict_list[predict_idx]:
                if correct_idx == predict_idx:
                    ret += 3
                else:
                    ret += 1
    return ret


# 정답 입력받기
correct = int(input())

score = 0

for i in range(5):
    # 예측값 입력받기
    predict = int(input())
    # number_baseball 호출해봅시다.
    score += number_baseball(correct, predict)

print(score)