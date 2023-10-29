from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((cost, y))
    graph[y].append((cost, x))
    
heap = []
visit_list = [[] for _ in range(N + 1)] 
dist = [float('inf')] * (N + 1)
heapq.heappush(heap, (0, A))
dist[A] = 0
visit_list[A].append((0, 0))


while heap:
    c, v = heapq.heappop(heap)
    if dist[v] < c:
        continue
    for nc, nv in graph[v]:
        if dist[nv] > c + nc:
            dist[nv] = c + nc
            heapq.heappush(visit_list[nv], (c + nc, max(heapq.nsmallest(1, visit_list[v])[0][1], nc)))
            heapq.heappush(heap, (c + nc, nv))
            
ans = float('inf')
while visit_list[B]:
    res = heapq.heappop(visit_list[B])   
    if res[0] <= C and ans > res[1]:
        ans = res[1]

if ans == float('inf'):
	print(-1)
else:
	print(ans)