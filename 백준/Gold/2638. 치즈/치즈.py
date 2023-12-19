from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]
melt_time = 0

def air_cover_cnt(y, x, N, M):
    cnt = 0
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < M and graphs[ny][nx] == -1: # 주변 외부공기 갯수 체크
            cnt += 1
            
    return cnt


while True:
    melt_time += 1
    
    que = deque([])
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0 , 0]

    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    graphs[0][0] = -1
    que.append([0, 0]) # 방문 큐에 추가
    
    while que: # bfs 순회 시작
        y, x = que.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < M: 
                if not visited[ny][nx] and (graphs[ny][nx] == 0 or graphs[ny][nx] == -1): # 범위 내에 있으면,
                    visited[ny][nx] = True
                    graphs[ny][nx] = -1 # 외부공기는 -1로 인식해준다.
                    que.append([ny, nx])
      
    cheese = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] == 1 and air_cover_cnt(i, j, N, M) > 1: # 치즈면서, 주변 공기가 2개 이상이면
                cheese.append([i, j])
                
    for i in cheese:
        graphs[i[0]][i[1]] = -1
        
    flag = False
    for i in range(N):
        for j in range(M):
            if graphs[i][j] == 1:
                flag = True
                
    if not flag:
        break

print(melt_time)