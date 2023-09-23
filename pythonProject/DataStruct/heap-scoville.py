import heapq

scoville = input() # "1 3 5 1 2 3"
K = input() # "100"

scoville = list(map(int, scoville.split(' ')))
K = int(K)

# scoville = [1,3,5,1,2,3]

heap = []
for num in scoville:
    heapq.heappush(heap, num)

mix_cnt = 0
while heap[0] < K:
    # heap의 top이 K보다 작으면 계속 반복.
    try:
        f1 = heapq.heappop(heap)
        f2 = heapq.heappop(heap)
        new_scoville = f1 + 2*f2
        heapq.heappush(heap, new_scoville)
        mix_cnt += 1
    except:
        # 예외가 발생하면 여기를 실행해라.
        # Index Out (배열 밖에 있는 데이터 참조)
        # 재귀함수 너무 많이 불렀을 때.
        # exit
        print("-1")
        exit(-1) # -1이 error라는 암묵적인 룰.
print(mix_cnt)
