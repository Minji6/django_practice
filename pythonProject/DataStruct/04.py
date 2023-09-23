'''reverse(“ABCDE”) = EDCBA
reverse(“KAIST”) = TSIAK

문자열을 거꾸로 출력해보는 재귀함수를 만들어보세요.'''


def reverse(s):
    # TODO: 문자열을 거꾸로 출력하는 재귀함수를 만들어보세요.

    if s == "":
        return
    else:
        reverse(s[1:])
        print(s[0], end="")


sentence = "HELLO WORLD!"
reverse(sentence)