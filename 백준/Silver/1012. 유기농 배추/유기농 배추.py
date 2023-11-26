from collections import deque
T = int(input())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    graphs = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    baechus = []
    for _ in range(K):
        X, Y = map(int, input().split())
        graphs[Y][X] = 1
        baechus.append((Y, X))
    
    for baechu in baechus:
        y, x = baechu
        
        if not visited[y][x]:
            que = deque([(y, x)])
            visited[y][x] = True
            while que:
                v = que.popleft()
    
                for i in range(4):
                    if 0 <= v[0] + dy[i] < N and 0 <= v[1] + dx[i] < M and not visited[v[0]+dy[i]][v[1]+dx[i]] and graphs[v[0]+dy[i]][v[1]+dx[i]] == 1:
                        que.append((v[0]+dy[i], v[1]+dx[i]))
                        visited[v[0]+dy[i]][v[1]+dx[i]] = True
            else:
                cnt += 1
                    
    print(cnt)