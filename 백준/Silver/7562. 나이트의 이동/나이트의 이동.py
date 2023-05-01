from collections import deque

T = int(input())

for _ in range(T):
    L = int(input())
    cur = list(map(int, input().split(" ")))
    move = list(map(int, input().split(" ")))
    dy = [1, 2, 1, 2, -1, -2, -1, -2]
    dx = [-2, -1, 2, 1, -2, -1, 2, 1]

    visit = [[0 for _ in range(L)] for _ in range(L)]
    que = deque()
    que.append(cur)
    cnt = 0

    while que:
        y, x = que.popleft()
        if [y, x] == move:
            print(visit[y][x])
            break
        for i in range(8):
            if x+dx[i] < 0 or x+dx[i] >= L or y+dy[i] < 0 or y+dy[i] >= L:
                continue
            if visit[y+dy[i]][x+dx[i]] == 0:
                visit[y+dy[i]][x+dx[i]] = visit[y][x] + 1
                que.append([y+dy[i], x+dx[i]])