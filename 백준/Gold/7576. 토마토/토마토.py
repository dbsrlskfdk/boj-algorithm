from collections import deque

M, N = map(int, input().split())
tomato = []
que = deque()
for i in range(N):
	tmp = list(map(int, input().split()))
	for j in range(M):
		if tmp[j] == 1:
			que.append((i, j))
	tomato.append(tmp)
que.append(-1)

dx = [0 ,0, -1, 1]
dy = [-1, 1, 0, 0]
year = 0
while que:
	coord = que.popleft()
	if coord == -1:
		if not que:
			break
		que.append(-1)
		year += 1
		continue
	y, x = coord

	for i in range(4):
		if (0 <= y+dy[i] < N and 0 <= x+dx[i] < M) and tomato[y+dy[i]][x+dx[i]] == 0:
			tomato[y+dy[i]][x+dx[i]] = 1
			que.append((y+dy[i], x+dx[i]))
            
for i in range(N):
	for j in range(M):
		if tomato[i][j] == 0:
			year = -1
			break
print(year)