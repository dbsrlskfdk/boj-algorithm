from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graphs = defaultdict(list)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graphs[a].append((cost, b))
heap = []
dist_k = [[float('inf') for _ in range(k)] for _ in range(n + 1)]

dist_k[1][0] = 0
heapq.heappush(heap, (0, 1))

while heap:
    c, v = heapq.heappop(heap)
    
    for nc, nv in graphs[v]:
        if dist_k[nv][k-1] > (c + nc):
            dist_k[nv][k-1] = (c + nc)
            dist_k[nv].sort()
            heapq.heappush(heap, (c + nc, nv))
            
for i in range(1, n + 1):
    if dist_k[i][k-1] == float('inf'):
        print(-1)
    else:
        print(dist_k[i][k-1])