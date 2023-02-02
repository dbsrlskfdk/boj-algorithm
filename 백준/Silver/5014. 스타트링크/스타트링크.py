from collections import deque

F, S, G, U, D = map(int, input().split(" "))

graph = [0 for _ in range(1000_000 + 1)]
que = deque([S])

while que:
    t = que.popleft()
    
    tmp_floor = [t+U, t-D]
    
    for c in tmp_floor:
        if 1 <= c and c <= F:
            if graph[c] == 0 and c != S:
                graph[c] = graph[t] + 1
                que.append(c)
    
    if G in tmp_floor:
        break
        
if S == G:
    print(0)
else:
    if graph[G] == 0:
        print("use the stairs")
    else:
        print(graph[G])