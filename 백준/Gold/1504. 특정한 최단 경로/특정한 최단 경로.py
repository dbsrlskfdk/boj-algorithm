#%%
from collections import defaultdict
import heapq

def dijkstra(start, edges):
    distance = [float('inf')] * (N + 1)
    heap = []
    heapq.heappush(heap, (start, 0))
    while heap:
        v, d = heapq.heappop(heap)
        if distance[v] < d:
            continue
        distance[v] = d
        for nv, nd in edges[v]:
            if distance[nv] > d + nd:
                distance[nv] = d + nd
                heapq.heappush(heap, (nv, d + nd))
    return distance


N, E = map(int, input().split())
edges = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
v_1, v_2 = map(int, input().split())

one_start = dijkstra(1, edges)
v_1_start = dijkstra(v_1, edges)
v_2_start = dijkstra(v_2, edges)
ans = min(one_start[v_1] + v_1_start[v_2] + v_2_start[N], one_start[v_2] + v_2_start[v_1] + v_1_start[N])
if ans == float('inf'):
    print(-1)
else:
    print(ans)