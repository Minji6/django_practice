#입력 값 중 음수가 아닌 최소값과 인덱스를 찾아봅시다.
#입력: 10개의 정수를 입력으로 사용합니다. 입력된 순으로 인덱스는 0부터 시작됩니다.
#출력: 음수가 아닌 가장 작은 수와 인덱스를 차례로 출력합니다. 전부 음수일 경우 ‘전부 음수입니다.’를 출력합니다.

data_list = []

for i in range(10):
    data_list.append(int(input()))

is_exist=False
idx=0

for a in data_list:
    if a>=0:
        if not(is_exist):
            tmp = a
            tmp_idx = idx
            is_exist = True
        elif tmp>a:
            tmp = a
            tmp_idx = tmp
    idx+=1

if is_exist:
    print(tmp)
    print(tmp_idx)
else: print('전부 음수입니다.')