from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
start, end = map(int, input().split())

def dijkstra(start, end, edges):
    heap = [(start, 0)]
    distance = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)
    while heap:
        v, w = heapq.heappop(heap)
        if distance[v] < w and visited[v]:
            continue
        visited[v] = True
        for nv, nw in edges[v]:
            if distance[nv] > w + nw:
                distance[nv] = w + nw
                heapq.heappush(heap, (nv, distance[nv]))
    return distance[end]

print(dijkstra(start, end, edges))