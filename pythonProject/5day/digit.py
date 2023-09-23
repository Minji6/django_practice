'''십진법은 0~9의 digit을 늘어놓아 수를 표현합니다. 예를 들어, 197은 3개의 digit (1, 9, 7)으로 이루어져 있습니다.
마찬가지로 101은 2개의 digit (0,1)으로 이루어져 있습니다.

이 미션은 수를 하나 입력받고 사용한 digit의 수를 print로 출력해주면 됩니다.

Input으로 수를 하나 입력받습니다.
중복 없이 저장하는 자료구조를 통해 사용한 digit의 수를 구합니다.
Hint : set의 크기는 len()함수로 구할 수 있습니다.'''

n = int(input)
digit = {}
digit.append(n)

print(len(int(digit)))