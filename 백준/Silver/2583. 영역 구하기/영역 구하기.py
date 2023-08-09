from collections import deque

M, N, K = map(int, input().split(" "))
square_list= [list(map(int, input().split(" "))) for _ in range(K)]
visited = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
	for j in range(square_list[i][1], square_list[i][3]): # y좌표
		for k in range(square_list[i][0], square_list[i][2]): # x좌표
			visited[M-(j+1)][k] = 1
            
que = deque()
cnt = 0
area_list = []

for i in range(M):
	for j in range(N):
		if visited[i][j] == 0:
			que.append([i, j])
			visited[i][j] = 1

			area = 0
			while que:
				y, x = que.popleft()
				area += 1
				if y-1 >= 0 and visited[y-1][x] == 0:
					que.append([y-1, x])
					visited[y-1][x] = 1
				if y+1 < M and visited[y+1][x] == 0:
					que.append([y+1, x])
					visited[y+1][x] = 1
				if x-1 >= 0 and visited[y][x-1] == 0:
					que.append([y, x-1])
					visited[y][x-1] = 1
				if x+1 < N and visited[y][x+1] == 0:
					que.append([y, x+1])
					visited[y][x+1] = 1
			else:
				cnt += 1
				area_list.append(area)

area_list.sort()
print(cnt)
print(" ".join(map(str, area_list)))