import heapq, sys

input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    m, v = map(int, input().split())
    gems.append((m, v))
    
C = []
for _ in range(K):
    C.append(int(input()))
C.sort()
gems.sort()

total = 0
tmp = []
for capable in C:
    while gems and gems[0][0] <= capable:
        heapq.heappush(tmp, (-gems[0][1], gems[0][0]))
        heapq.heappop(gems)
    
    if tmp:
        total += -heapq.heappop(tmp)[0]
        
print(total)