from collections import deque

N, M, K = map(int, input().split())
maps = [[int(i) for i in input()] for _ in range(N)]
visited = [[[float('inf') for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

que = deque()
que.append([0, 0, 0])

visited[0][0][0] = 1
while que:
    y, x, c = que.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if not (ny == 0 and nx == 0):
                if not maps[ny][nx]: # 벽이 아니면
                    if visited[ny][nx][c] > visited[y][x][c] + 1:
                        visited[ny][nx][c] = visited[y][x][c] + 1
                        que.append([ny, nx, c])
                else: # 벽이면
                    if c < K:
                        if visited[ny][nx][c+1] > visited[y][x][c] + 1:
                            visited[ny][nx][c+1] = visited[y][x][c] + 1
                            que.append([ny, nx, c+1])

print(-1 if min(visited[N-1][M-1]) == float('inf') else min(visited[N-1][M-1]))