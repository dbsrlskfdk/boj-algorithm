import heapq

N = int(input())
nums = list(map(int, input().split(" ")))
heap = []
mask = [0] * N
for i, v in enumerate(nums):
    heapq.heappush(heap, (v, i))
    
idx = 0
while heap:
    _, i = heapq.heappop(heap)
    mask[i] = idx
    idx += 1
    
print(" ".join([str(i) for i in mask]))