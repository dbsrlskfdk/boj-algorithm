from collections import deque

N, M = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

cnt = 0
area = []
for i in range(N):
	for j in range(M):
		if graph[i][j] == 1 and not visited[i][j]:
			tmp_area = 0
			que = deque([(i, j)])

			while que:
				y, x = que.popleft()
				visited[y][x] = True
				if y-1 >= 0 and graph[y-1][x] == 1 and not visited[y-1][x]:
					que.append((y-1, x))
					tmp_area += 1
					visited[y-1][x] = True
				if y+1 < N and graph[y+1][x] == 1 and not visited[y+1][x]:
					que.append((y+1, x))
					tmp_area += 1
					visited[y+1][x] = True
				if x-1 >= 0 and graph[y][x-1] == 1 and not visited[y][x-1]:
					que.append((y, x-1))
					tmp_area += 1
					visited[y][x-1] = True
				if x+1 < M and graph[y][x+1] == 1 and not visited[y][x+1]:
					que.append((y, x+1))
					tmp_area += 1
					visited[y][x+1] = True
			else:
				cnt += 1
				tmp_area += 1
				area.append(tmp_area)
                
print(cnt)
if len(area) != 0:
	print(max(area))
else:
	print(0)