import heapq
from random import *


class Heap:
    def __init__(self):
        self.queue = []

    def swap(self, i, j):
        tmp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = tmp

    def insert(self, key):
        pass

    def pop(self):
        top = self.queue[0]
        self.swap(0, len(self.queue) - 1)
        self.queue.pop()
        self.heapify(0)
        return top

    def top(self):
        return self.queue[0]

    def heapify(self, i):
        pass

    def parent(self, idx):
        return (idx - 1) // 2

    def left(self, idx):
        return idx * 2 + 1

    def right(self, idx):
        return idx * 2 + 2


num_samples = 100
limit = 100000000
samples = []
for i in range(num_samples):
    samples.append(randint(1, limit))

heap = []
my_heap = Heap()

for i in range(num_samples):
    heapq.heappush(heap, (-samples[i], samples[i]))  # min heap
    my_heap.insert(samples[i])

all_pass = True
for i in range(num_samples):
    print(heap[0][1], my_heap.top())
    if heapq.heappop(heap)[1] != my_heap.pop():
        all_pass = False

if all_pass:
    print("pass")
else:
    print("fail")