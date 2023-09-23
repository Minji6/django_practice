from random import *
from copy import copy


def insertion_sort(arr):
    # TODO:
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr
                [j-1] #swap


arr = [3,6,1,2,3,34,68,3,44,23,12,4,466]
#selection_sort(arr)
# bubble_sort(arr)
arr = quick_sort(arr)
print(arr)

num_samples = 1000
samples = []
for i in range(num_samples):
    samples.append(randint(1, 10000))
samples_test = copy(samples)
print("Sample 생성 완료")

samples.sort()
insertion_sort(samples_test)
for i in range(len(samples)):
    if samples[i] != samples_test[i]:
        print("Fail")
        exit(-1)

print("Pass")