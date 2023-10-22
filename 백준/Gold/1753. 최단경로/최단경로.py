from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [float('inf')] * (V+1)
edges = defaultdict(list)
visited = [False] * (V+1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([v, w])
    
# 다익스트라
visited[start] = True
graph[start] = 0
heapq.heappush(heap, (0, start))

while heap:
    w, v = heapq.heappop(heap)
    if graph[v] < w and visited[v]:
        continue
    visited[v] = True
    for nv, nw in edges[v]:
        if graph[nv] > w + nw:
            graph[nv] = w + nw
            if not visited[nv]:
                heapq.heappush(heap, (w + nw, nv))

for i in range(1, V+1):
    if graph[i] == float('inf'):
        print('INF')
    else:
        print(graph[i])