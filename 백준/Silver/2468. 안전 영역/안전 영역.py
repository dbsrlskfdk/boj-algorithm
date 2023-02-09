from collections import deque

N = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(N)]

cnt = []
for c in range(0, 101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    tmp_cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > c and visited[i][j] == False:
                que = deque([(i, j)])
                visited[i][j] = True
                
                while que:
                    p, q = que.popleft()
                    if p-1 >= 0:
                        if graph[p-1][q] > c and visited[p-1][q] == False:
                            que.append((p-1, q))
                            visited[p-1][q] = True
                    if p+1 < N:
                        if graph[p+1][q] > c and visited[p+1][q] == False:
                            que.append((p+1, q))
                            visited[p+1][q] = True
                    if q-1 >= 0:
                        if graph[p][q-1] > c and visited[p][q-1] == False:
                            que.append((p, q-1))
                            visited[p][q-1] = True
                    if q+1 < N:
                        if graph[p][q+1] > c and visited[p][q+1] == False:
                            que.append((p, q+1))
                            visited[p][q+1] = True
                tmp_cnt += 1
    if tmp_cnt != 0:
        cnt.append(tmp_cnt)
 
print(max(cnt))
