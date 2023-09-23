from random import *
from copy import copy

def selection_sort(arr):
    # TODO:
    n = len(arr)
    for i in range(0, n-1):
        min_idx = None
        for j in range(i+1, n):
            if min_idx is None:
                min_idx = j
            else:
                if arr[j] < arr[min_idx]:
                    min_idx = j
        if arr[i] > arr[min_idx]:
            arr[i], arr[min_idx] = arr[min_idx]
            arr[i]

arr = [3,6,1,2,3,34,68,3,44,23,12,4,466]
selection_sort(arr)
print(arr)

num_samples = 1000
samples = []
for i in range(num_samples):
    samples.append(randint(1, 10000))
samples_test = copy(samples)
print("Sample 생성 완료")

samples.sort()
selection_sort(samples_test)
for i in range(len(samples)):
    if samples[i] != samples_test[i]:
        print("Fail")
        exit(-1)

print("Pass")