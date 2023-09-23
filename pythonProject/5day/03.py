#input을 통한 두 정수 a, b를 입력받아 words_list.txt에서 길이가 a이상 b이하인 단어의 개수를 출력해줍니다.

a = int(input())
b = int(input())

f = open("words_list.txt", "r")
total = 0

for line in f:
    word = line.strip()  # strip() 공백제거 함수

    # 길이가 a이상 b이하인 단어의 수를 구하는 코딩을 해봅시다.
    if (len(word) >= 3) and (len(word) <= 4):
        total +=1

f.close()
print(total)