from collections import deque

def bfs(y, x, graph, visited):
    que = deque([(y, x)])
    visited[y][x] = 1
    cnt = 0
    while que:
        p, q = que.popleft()
        cnt += 1
        if graph[p][q] == 1:
            if q-1 >= 0 and graph[p][q-1] == 1 and visited[p][q-1] == 0:
                visited[p][q-1] = 1
                que.append((p, q-1))
            if q+1 < N and graph[p][q+1] == 1 and visited[p][q+1] == 0:
                visited[p][q+1] = 1
                que.append((p, q+1))
            if p-1 >= 0 and graph[p-1][q] == 1 and visited[p-1][q] == 0:
                visited[p-1][q] = 1
                que.append((p-1, q))
            if p+1 < N and graph[p+1][q] == 1 and visited[p+1][q] == 0:
                visited[p+1][q] = 1
                que.append((p+1, q))
    return cnt

N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
graph = []
for _ in range(N):
    tmp = input()
    tmp_list = []
    
    for c in tmp:
        tmp_list.append(int(c))
    graph.append(tmp_list)
    
num_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = bfs(i, j, graph, visited)
            if cnt != 0:
                num_list.append(cnt)
num_list.sort()

print(len(num_list))
for i in num_list:
    print(i)