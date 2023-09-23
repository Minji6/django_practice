import heapq

N = int(input())
left_heap = []  # max heap
right_heap = []  # min heap
output = []
for i in range(N):
    input_num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-input_num, input_num))

    else:  # len(left_heap) != len(right_heap)
        heapq.heappush(right_heap, (input_num, input_num))

    if right_heap:
        # 오른쪽에 원소가 없으면 왼쪽에만 존재.
        # 왼쪽에 있는 걸 그냥 가져다 출력.
        # 오른쪽에 있으면 비교를 해봐야 해요.
        left_top = left_heap[0][1]  # tuple[-,+]
        right_top = right_heap[0][1]
        if left_top > right_top:
            max_v = heapq.heappop(left_heap)[1]
            min_v = heapq.heappop(right_heap)[1]
            heapq.heappush(left_heap, (-min_v, min_v))
            heapq.heappush(right_heap, (max_v, max_v))

    output.append(left_heap[0][1])
print(output)