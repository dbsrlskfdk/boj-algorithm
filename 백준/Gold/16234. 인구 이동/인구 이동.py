from collections import deque

def bfs():
    visited = [[False] * N for _ in range(N)]
    union_country = []
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]


    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                que = deque([[i, j]])
                temp_union = [[i, j]]
                visited[i][j] = True

                while que:
                    y, x = que.popleft()
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N:
                            if not visited[ny][nx] and L <= abs(arrs[y][x] - arrs[ny][nx]) <= R:
                                que.append([ny, nx])
                                temp_union.append([ny, nx])
                                visited[ny][nx] = True

                union_country.append(temp_union)

    for uni in union_country:
        total_union = 0
        cnt_union = 0
        for i, j in uni:
            cnt_union += 1
            total_union += arrs[i][j]

        mean_population = int(total_union/cnt_union)
        for i, j in uni:
            arrs[i][j] = mean_population

    if len(union_country) == N**2: # union_country의 갯수가 개별의 나라 갯수와 같다면, 업데이트 된게 없다는것
        return False
    else:
        return True


N, L, R = map(int, input().split())

arrs = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while bfs():
    cnt += 1

print(cnt)