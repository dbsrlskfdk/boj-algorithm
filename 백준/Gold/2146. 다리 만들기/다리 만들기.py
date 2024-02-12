from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False] * N for _ in range(N)]

def bfs(st, num):
    que = deque([st])
    while que:
        y, x = que.popleft()
        
        maps[y][x] = num
        
        for h in range(4):
            ny = y + dy[h]
            nx = x + dx[h]
            
            if 0 <= ny < N and 0 <= nx < N:
                if maps[ny][nx]: # 땅이면
                    if not visited[ny][nx]:
                        que.append([ny, nx])
                        visited[ny][nx] = True
                        
island_num = 2
min_dist = float('inf')
for i in range(N):
    for j in range(N):
        if maps[i][j] and not visited[i][j]: # 섬 번호들 2 ~ 다시 붙이기
            bfs([i, j], island_num)
            island_num += 1
        
        if maps[i][j]: # 반복 진행하면서 섬이면,
            br_que = deque([[i, j]])
            br_visited = [[0] * N for _ in range(N)]
            
            while br_que:
                by, bx = br_que.popleft()
                    
                if br_visited[by][bx] > min_dist:
                    break
                    
                for h in range(4):
                    nby = by + dy[h]
                    nbx = bx + dx[h]
                    
                    if (0 <= nby < N and 0 <= nbx < N) and not br_visited[nby][nbx]:
                        if maps[nby][nbx] == 0:
                            br_que.append([nby, nbx])
                            br_visited[nby][nbx] = br_visited[by][bx] + 1
                        elif maps[i][j] != maps[nby][nbx]:
                            min_dist = min(min_dist, br_visited[by][bx])
              
print(min_dist)