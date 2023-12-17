import heapq

W, H = map(int, input().split())
graphs = []
lazor_C = []
for i in range(H):
    tmp = [c for c in input()]
    for j, v in enumerate(tmp):
        if v == "C":
            lazor_C.append((i, j))
        else:
            continue
    graphs.append(tmp)
    
visited = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]
heap = []
for i in range(4):
    visited[lazor_C[0][0]][lazor_C[0][1]][i] = 0
heapq.heappush(heap, (0, (lazor_C[0][0], lazor_C[0][1])))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

while heap:
    c, (y, x) = heapq.heappop(heap)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= nx < W and 0 <= ny < H and graphs[ny][nx] != "*":
            for j in range(4):
                if i != j:
                    if visited[ny][nx][i] > visited[y][x][j] + 1:
                        visited[ny][nx][i] = visited[y][x][j] + 1
                        heapq.heappush(heap, (visited[ny][nx][i], (ny, nx)))
                else:
                    if visited[ny][nx][i] > visited[y][x][i]:
                        visited[ny][nx][i] = visited[y][x][i]
                        heapq.heappush(heap, (visited[ny][nx][i], (ny, nx)))
                        
print(min(visited[lazor_C[1][0]][lazor_C[1][1]]))