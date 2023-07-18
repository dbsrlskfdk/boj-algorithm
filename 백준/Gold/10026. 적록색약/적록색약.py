#%%
from collections import deque
#%%
N = int(input())
#%%
arr = [[i for i in input()] for _ in range(N)]
#%%
que = deque()
visited = [[0]*N for _ in range(N)]
#%%
red_green = 0
none_red_green = 0
#%%
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			que.append((i, j))
			visited[i][j] = 1
			cur_color = arr[i][j]
			while que:
				# print(que)
				y, x = que.popleft()
				for p in range(4):
					if 0 <= y + dy[p] < N and 0 <= x + dx[p] < N:
						if cur_color == 'R' or cur_color == 'G':
							if visited[y+dy[p]][x+dx[p]] == 0 and (arr[y+dy[p]][x+dx[p]] == 'R' or arr[y+dy[p]][x+dx[p]] == 'G'):
								visited[y+dy[p]][x+dx[p]] = 1
								que.append((y+dy[p], x+dx[p]))
						else:
							if visited[y+dy[p]][x+dx[p]] == 0 and arr[y+dy[p]][x+dx[p]] == 'B':
								visited[y+dy[p]][x+dx[p]] = 1
								que.append((y+dy[p], x+dx[p]))
			else:
				red_green += 1
#%%
que = deque()
visited = [[0]*N for _ in range(N)]
#%%
for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			que.append((i, j))
			visited[i][j] = 1
			cur_color = arr[i][j]
			while que:
				# print(que)
				y, x = que.popleft()
				for p in range(4):
					if 0 <= y + dy[p] < N and 0 <= x + dx[p] < N:
						if visited[y+dy[p]][x+dx[p]] == 0 and arr[y+dy[p]][x+dx[p]] == cur_color:
							visited[y+dy[p]][x+dx[p]] = 1
							que.append((y+dy[p], x+dx[p]))
			else:
				none_red_green += 1
#%%
print(none_red_green, red_green)
#%%
