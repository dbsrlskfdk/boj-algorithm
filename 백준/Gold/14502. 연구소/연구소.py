from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
safe_area = []
max_cnt = 0

def bfs(v):
    global tmp_nums
    que = deque([v])    
    while que:
        y, x = que.popleft()
        visited[y][x] = True
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and tmp_nums[ny][nx] == 0:
                visited[ny][nx] = True
                tmp_nums[ny][nx] = 2
                que.append((ny, nx))
                
for i in range(N):
    for j in range(M):
        if nums[i][j] == 0:
            safe_area.append((i, j))
            
for walls in combinations(safe_area, 3):
    visited = [[False] * M for _ in range(N)]
    tmp_nums = copy.deepcopy(nums)
    cnt = 0
    for wall in walls:
        tmp_nums[wall[0]][wall[1]] = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and nums[i][j] == 2:
                bfs((i, j))
    
    
    for i in range(N):
        for j in range(M):
            if tmp_nums[i][j] == 0:
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)