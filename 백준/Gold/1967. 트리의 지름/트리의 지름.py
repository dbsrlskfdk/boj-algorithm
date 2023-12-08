from collections import defaultdict

n = int(input())
graphs = defaultdict(list)

for _ in range(n-1):
    v, u, w = map(int, input().split())
    graphs[v].append((u, w))
    graphs[u].append((v, w))
    
stack = []
dist = [0] * (n+1)
stack.append((1, 0))
dist[1] = 0
max_v = -1
max_dist = 0

while stack:
    v, w = stack.pop()
   # print(f"Visited Node : {v}")
    for nv, nw in graphs[v]:
        if nv != 1 and not dist[nv]:
            dist[nv] = dist[v] + nw
            if dist[nv] > max_dist:
                max_dist = dist[nv]
                max_v = nv
            # print(f"Refresh node : {nv}, Weight : {dist[nv]}")
            
            stack.append((nv, nw))
    # print("======")
    
stack = []
dist = [0] * (n+1)
stack.append((max_v, 0))
dist[max_v] = 0
max_dist = 0

while stack:
    v, w = stack.pop()
    # print(f"Visited Node : {v}")
    for nv, nw in graphs[v]:
        if nv != max_v and not dist[nv]:
            dist[nv] = dist[v] + nw
            if dist[nv] > max_dist:
                max_dist = dist[nv]
            # print(f"Refresh node : {nv}, Weight : {dist[nv]}")
            
            stack.append((nv, nw))
    # print("======")
    
print(max_dist)