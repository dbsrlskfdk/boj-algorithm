from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]

cnt_Y = 0 # 지난 년수
cnt = 0 # 빙산 갯수 초기화용
while cnt < 2 : # 센티널 벨류가 cnt가 2보다 작을 때
    cnt = 0 # 다음 iter때 빙산 갯수 초기화 필요
    visited = [[False] * M for _ in range(N)]
    dec_cnt = [[0] * M for _ in range(N)]

    cnt_Y += 1 # 년수가 지난거니까..
    # zero_cnt = 0 #0 세기용도

    for i in range(1, N-1):
            for j in range(1, M-1):
                if graph[i][j] != 0 and not visited[i][j]: #수정 전(graph)의 값이 0이 아니면,
                    que = deque([(i, j)])
                    while que:
                        a, b = que.popleft()
                        visited[a][b] = True
                        if a-1 >= 0:
                            if graph[a-1][b] != 0 and not visited[a-1][b]:
                                visited[a-1][b] = True
                                que.append((a-1, b))
                            elif graph[a-1][b] == 0:
                                dec_cnt[a][b] += 1
                        if a+1 < N:
                            if graph[a+1][b] != 0 and not visited[a+1][b]:
                                visited[a+1][b] = True
                                que.append((a+1, b))
                            elif graph[a+1][b] == 0:
                                dec_cnt[a][b] += 1
                        if b-1 >= 0:
                            if graph[a][b-1] != 0 and not visited[a][b-1]:
                                visited[a][b-1] = True
                                que.append((a, b-1))
                            elif graph[a][b-1] == 0:
                                dec_cnt[a][b] += 1
                        if b+1 < M:
                            if graph[a][b+1] != 0 and not visited[a][b+1]:
                                visited[a][b+1] = True
                                que.append((a, b+1))
                            elif graph[a][b+1] == 0:
                                dec_cnt[a][b] += 1
                    else:
                        cnt += 1


    for i in range(1, N-1):
        for j in range(1, M-1):
            graph[i][j] -= dec_cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(cnt_Y-1)
        break