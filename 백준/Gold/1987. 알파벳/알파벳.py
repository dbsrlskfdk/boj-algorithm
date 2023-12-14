from collections import defaultdict
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
alpha_sort = set()
boards = []
for _ in range(R):
    tmp = []
    for c in input():
        alpha_sort.add(c)
        tmp.append(c)
    boards.append(tmp)
    
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
max_cnt = 0
visited = set()
visited.add(boards[0][0])
len_alpha_sort = len(alpha_sort)

def dfs(st, cnt, visited):
    global max_cnt
    # print(*arr, cnt)
    max_cnt = max(max_cnt, cnt)
    y, x = st
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if not boards[ny][nx] in visited:
                visited.add(boards[ny][nx])
                dfs([ny, nx], cnt+1, visited)
                visited.discard(boards[ny][nx])  
    return


dfs([0, 0], 1, visited)
print(max_cnt)