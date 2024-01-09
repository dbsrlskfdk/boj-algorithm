from collections import deque, defaultdict
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
orders = defaultdict(int)
graphs = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    orders[b] += 1
    
que = deque()
for i in range(1, N+1):
    if not orders[i]:
        que.append(i)
        
while que:
    v = que.popleft()
    print(v, end=" ")
    for nv in graphs[v]:
        orders[nv] -= 1
        
        if orders[nv] == 0:
            que.append(nv)