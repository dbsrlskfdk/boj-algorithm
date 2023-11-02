from collections import defaultdict
import heapq

N, M, K = map(int, input().split())
graphs = defaultdict(list)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graphs[a].append((cost, b))
    graphs[b].append((cost, a))
    
heap = []
dist = [[float('inf')] * (K + 1) for _ in range(N + 1)]

heapq.heappush(heap, (0, 1, 0))

while heap:
    nc, nv, n_mask = heapq.heappop(heap)
    if dist[nv][n_mask] < nc:
        continue
    for c, v in graphs[nv]:
        if n_mask < K:
            if dist[v][n_mask + 1] > nc:
                dist[v][n_mask + 1] = nc
                heapq.heappush(heap, (nc, v, n_mask + 1))
            if dist[v][n_mask] > nc + c:
                dist[v][n_mask] = nc + c
                heapq.heappush(heap, (nc + c, v, n_mask))
        else:
            if dist[v][n_mask] > nc + c:
                dist[v][n_mask] = nc + c
                heapq.heappush(heap, (nc + c, v, n_mask))

                
print(min(dist[N]))