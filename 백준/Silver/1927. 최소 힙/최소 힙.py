import heapq, sys

input = sys.stdin.readline

N = int(input())
heap = []
cnt = 0

for _ in range(N):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap)) if cnt != 0 else print(0)
        cnt = max(0, cnt-1)
    else:
        heapq.heappush(heap, x)
        cnt += 1