from collections import deque

n, m = map(int, input().split(" "))
graphs = [list(map(int, input().split(" "))) for _ in range(n)]

st = -1
flag = False
for i in range(n):
    for j in range(m):
        if graphs[i][j] == 2:
            st = (i, j)
            flag = True
            break
    if flag:
        break
        
visited = [[0] * m for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
que = deque([st])
visited[st[0]][st[1]] = 0

while que:
    y, x = que.popleft()
    
    for i in range(4):
        if (0 <= y+dy[i] < n and 0 <= x+dx[i] < m) and graphs[y+dy[i]][x+dx[i]] != 0:
            if not visited[y+dy[i]][x+dx[i]] and not (y+dy[i] == st[0] and x+dx[i] == st[1]):
                visited[y+dy[i]][x+dx[i]] = visited[y][x] + 1
                que.append((y+dy[i], x+dx[i]))
                
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and (graphs[i][j] != 0 and graphs[i][j] != 2):
            visited[i][j] = -1

for item in visited:
    print(*item)