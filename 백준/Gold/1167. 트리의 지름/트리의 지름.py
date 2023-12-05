from collections import defaultdict

V = int(input())
graphs = defaultdict(list)

for _ in range(V):
    conn = list(map(int, input().split()))
    for i in range(1, len(conn)-1, 2):
        graphs[conn[0]].append((conn[i+1], conn[i]))
        
stack = []
visited = [0] * (V+1)
max_distance = 0
max_v = 0
st = 1
stack = [st]

while stack:
    v = stack.pop()
    
    for dist, nv in graphs[v]:
        if not visited[nv] and nv != st:
            visited[nv] = visited[v] + dist
            if max_distance < visited[nv]:
                max_distance = visited[nv]
                max_i = nv
            stack.append(nv)
            
max_distance = 0
stack = []
visited = [0] * (V+1)
stack = [max_i]

while stack:
    v = stack.pop()
    
    for dist, nv in graphs[v]:
        if not visited[nv] and nv != max_i:
            visited[nv] = visited[v] + dist
            max_distance = max(max_distance, visited[nv])
            stack.append(nv)
            
print(max_distance)