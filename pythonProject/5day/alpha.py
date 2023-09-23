'''사용한 알파벳 수 구하기
abdidcj와 같은 공백이 없고 소문자 알파벳으로만 이루어진 문자열이 입력으로 들어올 때, 사용된 알파벳 수를 구하세요.'''

n = str(input())

alpha_len = len(set(n))

print(alpha_len)