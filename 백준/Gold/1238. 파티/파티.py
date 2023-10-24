from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N, M, X = map(int, input().split())
go_edges = defaultdict(list)
back_edges = defaultdict(list)

for _ in range(M):
    a, b, dist = map(int, input().split())
    go_edges[b].append((a, dist))
    back_edges[a].append((b, dist))
    
def dijkstra(st, edges):
    heap = []
    distance = [float('inf')] * (N + 1)
    
    heapq.heappush(heap, (st, 0))
    while heap:
        v, t = heapq.heappop(heap)
        if distance[v] < t:
            continue
        for nv, nt in edges[v]:
            if distance[nv] > t + nt:
                distance[nv] = t + nt
                heapq.heappush(heap, (nv, t + nt)) 
    return distance

go_distance = dijkstra(X, go_edges)
back_distance = dijkstra(X, back_edges)
total_distance = [go_distance[i] + back_distance[i] for i in range(1, N + 1) if i != X]

print(max(total_distance))