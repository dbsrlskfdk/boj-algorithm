import sys
import heapq

from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

graphs = defaultdict(list)
orders = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    orders[b] += 1

que = []
for i in range(1, N+1):
    if not orders[i]:
        heapq.heappush(que, i)

while que:
    v = heapq.heappop(que)
    
    print(v, end=" ")
    for nv in graphs[v]:
        orders[nv] -= 1
    
        if orders[nv] == 0:
            heapq.heappush(que, nv)