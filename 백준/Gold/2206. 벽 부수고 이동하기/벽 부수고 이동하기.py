from collections import deque

N, M = map(int, input().split())
graphs = [[int(i) for i in input()] for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
visited = [[[0, 0] for _ in range(M)]  for _ in range(N)]
que = deque([(0, 0, False)])
visited[0][0] = [1, 1]

while que:
    y, x, flag = que.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < M:
            if not flag: # 이전 탐색 노드가 벽이 아니면(flag=False),
                if not graphs[ny][nx]: # 다음 노드가 벽이 아니면
                    if not visited[ny][nx][0]:
                        visited[ny][nx][0] = visited[y][x][0] + 1
                        que.append((ny, nx, False))
                else: # 다음 노드가 벽이면
                    if not visited[ny][nx][1]:
                        visited[ny][nx][1] = visited[y][x][0] + 1
                        que.append((ny, nx, True))
            else: # 이전 탐색 노드가 벽이면(flag=True)
                if not graphs[ny][nx] and not visited[ny][nx][1]: # 그다음 노드가 벽이 아닐 때만 갱신
                    visited[ny][nx][1] = visited[y][x][1] + 1
                    que.append((ny, nx, True))
                    
print(min(visited[N-1][M-1]) if visited[N-1][M-1][0] and visited[N-1][M-1][1] else -1 if not visited[N-1][M-1][0] and not visited[N-1][M-1][1] else max(visited[N-1][M-1]))