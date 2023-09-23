'''length(“STRING”) = 6
length(“HELLO WORLD!”) = 12

문자열의 길이를 구해주는 함수를 재귀함수를 이용해 구현해보세요.'''


def length(s):
    # TODO: 문자열의 길이를 재귀함수를 이용해 구해보세요.
    length = 0
    if s == 0:
        return 0
    else:
        return 1 + length(s[1:])


sentence = "HELLO WORLD!"
res = length(sentence)
print(res)