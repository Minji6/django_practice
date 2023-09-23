'''글자 세기(Syllable Count)
텍스트 파일에 있는 글자의 수를 세봅시다.

사전을 만들어서 각 글자의 개수를 구하세요.
처음 나온 글자면 key부터 만들어야 합니다.
입력된 글자가 주어진 text.txt파일에 몇 개가 있는지 출력하세요.
만약 입력된 글자가 text.txt에 없다면, 0을 출력해야 합니다.'''

# 기본 코드입니다.

import os
import sys

letters = {}
f = open('text.txt')
while True:
    line = f.readline()
    # 여기서부터 코딩하시면 됩니다.

    if not line:
        break

    for ch in line:
        if (ch == ' ') or (ch == '\n'):
            continue

        if ch in letters.keys():
            # 특정 글자가 키에 있을 경우
            letters[ch] += 1
        else:
            # 아직 키가 없는 경우, 처음 나온 경우
            letters[ch] = 1

print(letters[input()])

f.close()