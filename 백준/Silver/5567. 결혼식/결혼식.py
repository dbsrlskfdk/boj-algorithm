from collections import defaultdict, deque

N = int(input())
M = int(input())

graph = defaultdict(list)
que = deque()
cnt = 0
visited = [False] * (N+1)
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
if graph[1]:
    visited[1] = True
    depth = 0
    
    for v in graph[1]:
        que.append(v)    
    que.append(-1)
        
    while que:
        v = que.popleft()
        
        if v != -1 and visited[v] == False:
            cnt += 1
            visited[v] = True
            que.extend(graph[v])
        elif v == -1:
            if depth != 1:
                depth += 1
                que.append(-1)
            else:
                break
print(cnt)