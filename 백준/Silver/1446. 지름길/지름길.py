import heapq
from collections import defaultdict

N, D = map(int, input().split())
weights = defaultdict(list)
for _ in range(N):
    st, ed, w = map(int, input().split())
    if ed <= D:
        weights[st].append((w, ed))
        
visited = [False for _ in range(D+1)]
distance = [float('inf') for _ in range(D+1)]
distance[0] = 0
visited[0] = True
que = []
heapq.heappush(que, (0, 0))

while que:
    W, V = heapq.heappop(que)

    if distance[V] < W:
        continue
    
    visited[V] = True
    if weights[V]:
        for nw, nv in weights[V]:
            if distance[nv] > W + nw:
                distance[nv] = W + nw
                if not visited[nv]:
                    heapq.heappush(que, (W+nw, nv))

    if V+1 <= D and distance[V+1] > W + 1:
        distance[V+1] = W + 1
        if not visited[V+1]:
            heapq.heappush(que, (W+1, V+1))

print(distance[D])