from collections import deque

def bfs(v, floors, e):
    dx = [1, -1]
    dy = [1, -1]
    dz = [1, -1]
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    que = deque([v])
    while que:
        l, r, c = que.popleft()
        
        for i in range(2):
            if 0 <= l + dz[i] < L:
                if floors[l + dz[i]][r][c] != '#' and not visited[l + dz[i]][r][c]:
                    visited[l + dz[i]][r][c] = visited[l][r][c] + 1
                    que.append((l + dz[i], r, c))
            if 0 <= r + dy[i] < R:
                if floors[l][r + dy[i]][c] != '#' and not visited[l][r + dy[i]][c]:
                    visited[l][r + dy[i]][c] = visited[l][r][c] + 1
                    que.append((l, r + dy[i], c))
            if 0 <= c + dx[i] < C:
                if floors[l][r][c + dx[i]] != '#' and not visited[l][r][c + dx[i]]:
                    visited[l][r][c + dx[i]] = visited[l][r][c] + 1
                    que.append((l, r, c + dx[i]))            
    return visited[e[0]][e[1]][e[2]]

L, R, C = map(int, input().split())

while L != 0 and R != 0 and C != 0:
    start = 0
    end = 0
    floors = []
    for i in range(L):
        floor = []
        for j in range(R):
            tmp = []
            for k, c in enumerate(input()):
                if c == 'S':
                    start = (i, j, k)
                elif c == 'E':
                    end = (i, j, k)
                tmp.append(c)
            floor.append(tmp)
        input()
        floors.append(floor)
    ans = bfs(start, floors, end)
    if ans:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')
        
    L, R, C = map(int, input().split())