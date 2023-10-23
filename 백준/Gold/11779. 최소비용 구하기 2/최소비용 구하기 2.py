from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
edges = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
start, end = map(int, input().split())

graph = [float('inf')] * (n + 1)
route = [[start] for _ in range(n + 1)]
visited = [False] * (n + 1)
heap = []

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
            route[nv] = route[v] + [nv]
            if not visited[nv]:
                heapq.heappush(heap, (w + nw, nv))
                
print(graph[end])
print(len(route[end]))
print(*route[end])