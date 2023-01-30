from collections import deque
def bfs(graph, visited, N, M):
    que = deque([(0, 0)])
    
    while que:
        y, x = que.popleft()
        if x-1 >= 0 and graph[y][x-1] == 1 and visited[y][x-1] == 0:
            visited[y][x-1] = visited[y][x] + 1
            que.append((y, x-1))
        if x+1 < M and graph[y][x+1] == 1 and visited[y][x+1] == 0:
            visited[y][x+1] = visited[y][x] + 1
            que.append((y, x+1))
        if y-1 >= 0 and graph[y-1][x] and visited[y-1][x] == 0:
            visited[y-1][x] = visited[y][x] + 1
            que.append((y-1, x))
        if y+1 < N and graph[y+1][x] and visited[y+1][x] == 0:
            visited[y+1][x] = visited[y][x] + 1
            que.append((y+1, x))
            
N, M = map(int, input().split(" "))

graph = []
for _ in range(N):
    tmp = input()
    tmp_list = []
    for c in tmp:
        tmp_list.append(int(c))
    graph.append(tmp_list)

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

bfs(graph, visited, N, M)
print(visited[N-1][M-1])