from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
S, D = map(int, input().split())

graphs = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split())
    graphs[a].append((b, w))
    graphs[b].append((a, w))
    
dist = [[float('inf')] * N for _ in range(N + 1)]
dist[S][0] = 0
heap = []
heapq.heappush(heap, (0, S, 0))

while heap:
    c, v, through_num = heapq.heappop(heap)
    flag = False
    
    for i in range(through_num):
        if dist[v][i] < c:
            flag = True
            break
            
    if flag or dist[v][through_num] < c or not(through_num < N-1):
        continue
    for nv, nc in graphs[v]:
        if dist[nv][through_num+1] > dist[v][through_num] + nc:
            dist[nv][through_num+1] = dist[v][through_num] + nc
            heapq.heappush(heap, (dist[nv][through_num+1], nv, through_num + 1))
            
            
for i in range(K+1):
    k = 0 if i == 0 else int(input())
    ans = float('inf')
    for j in range(N):
        dist[D][j] += j * k
        ans = min(ans, dist[D][j])
    print(ans)