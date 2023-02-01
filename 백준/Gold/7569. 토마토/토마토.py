from collections import deque
import copy

M, N, H = map(int, input().split(" "))
tomato = []
tomato_que = deque()
for h in range(H):
    tmp = [] # h의 차원 담당
    for n in range(N):
        tmp.append(list(map(int, input().split(" "))))
        for m in range(M):
            if tmp[n][m] == 1:
                tomato_que.append((h, n, m))

    tomato.append(tmp)
tomato_que.append(-1)

cnt = 0
while tomato_que:
    coord = tomato_que.popleft()
    
    if coord == -1:
        if not tomato_que:
            break
        tomato_que.append(-1)
        cnt += 1
        continue
            
    h, n, m = coord
    if m-1 >= 0 and tomato[h][n][m-1] == 0:
            tomato[h][n][m-1] = 1
            tomato_que.append((h, n, m-1))
    if m+1 < M and tomato[h][n][m+1] == 0:
            tomato[h][n][m+1] = 1
            tomato_que.append((h, n, m+1))
    if n-1 >= 0 and tomato[h][n-1][m] == 0:
            tomato[h][n-1][m] = 1
            tomato_que.append((h, n-1, m))
    if n+1 < N and tomato[h][n+1][m] == 0:
            tomato[h][n+1][m] = 1
            tomato_que.append((h, n+1, m))
    if h-1 >= 0 and tomato[h-1][n][m] == 0:
            tomato[h-1][n][m] = 1
            tomato_que.append((h-1, n, m))
    if h+1 < H and tomato[h+1][n][m] == 0:
            tomato[h+1][n][m] = 1
            tomato_que.append((h+1, n, m))
            
for h in range(H):
    for n in range(N):
        if 0 in tomato[h][n]:
            cnt = -1

print(cnt)            