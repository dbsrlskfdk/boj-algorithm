from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
distance_list = [0 for _ in range(N)]
def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                distance_list[i] = distance_list[v] + 1
                
bfs(graph, 0, [False] * N)
max_dist = max(distance_list)
cnt = 0
min_node = 0
for i in range(N):
    if distance_list[i] == max_dist:
        cnt += 1
        if min_node == 0:
            min_node = i
            
print(min_node + 1, max_dist, cnt)