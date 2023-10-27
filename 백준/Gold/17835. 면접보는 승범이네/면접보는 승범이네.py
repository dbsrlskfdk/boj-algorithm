from collections import defaultdict
import heapq

def dijkstra(interview_city, edges):
    heap = []
    dist = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)

    for t in interview_city:
        heapq.heappush(heap, (0, t))
        dist[t] = 0
        visited[t] = True
        
    while heap:
        c, v = heapq.heappop(heap)
        if dist[v] < c and visited[v]:
            continue
        visited[v] = True
        for nc, nv in edges[v]:
            if dist[nv] > c + nc:
                dist[nv] = c + nc
                if not visited[nv]:
                    heapq.heappush(heap, (c + nc, nv))
    return dist
    
N, M, K = map(int, input().split())
edges = defaultdict(list)

for _ in range(M):
    U, V, C = map(int, input().split())
    edges[V].append((C, U))
interviews = list(map(int, input().split()))

res = dijkstra(interviews, edges)
max_distance = -1
max_i = 0
for i in range(1, N + 1):
    if res[i] > max_distance:
        max_distance = res[i]
        max_i = i

print(max_i)
print(max_distance)