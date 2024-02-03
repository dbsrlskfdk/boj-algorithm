from collections import deque

N, M = map(int, input().split())
maps = []
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == "R":
            ry, rx = i, j
        elif tmp[j] == "B":
            by, bx = i, j
    maps.append(tmp)
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

def move(y, x, i):
    mv_cnt = 0

    while maps[y + dy[i]][x + dx[i]] != "#" and maps[y][x] != "O":
        y += dy[i]
        x += dx[i]
        mv_cnt += 1

    return y, x, mv_cnt


que = deque([[ry, rx, by, bx, 1]])
visited = [[ry, rx, by, bx]]
flag = False

while que:
    ry, rx, by, bx, cnt = que.popleft()
    
    if cnt > 10:
        print(-1)
        break
        
    for i in range(4):
        nry, nrx, rcnt = move(ry, rx, i)
        nby, nbx, bcnt = move(by, bx, i)
        
        if maps[nby][nbx] == "O":
            continue
        if maps[nry][nrx] =="O":
            flag = True
            print(cnt)
            break

        if nry == nby and nrx == nbx:
            if rcnt > bcnt:
                nry -= dy[i]
                nrx -= dx[i]
            else:
                nby -= dy[i]
                nbx -= dx[i]
        
        if [nry, nrx, nby, nbx] not in visited:
            visited.append([nry, nrx, nby, nbx])
            que.append([nry, nrx, nby, nbx, cnt+1])

    
    if flag:
        break
else:
    print(-1)