import heapq

M, N = map(int, input().split())
graph = [[int(i) for i in input()] for _ in range(N)]
cost = [[float('inf')] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
heap = [(0, (0, 0))]
cost[0][0] = 0
visited[0][0] = True

while heap:
    c, (y, x) = heapq.heappop(heap)
    if cost[y][x] < c and visited[y][x]:
        continue
    visited[y][x] = True
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= y + dy < N and 0 <= x + dx < M:
            if graph[y+dy][x+dx] == 1:
                if cost[y+dy][x+dx] > c + 1:
                    cost[y+dy][x+dx] = c + 1
                    if not visited[y+dy][x+dx]:
                        heapq.heappush(heap, (c+1, (y+dy, x+dx)))
            elif graph[y+dy][x+dx] == 0:
                if cost[y+dy][x+dx] > c:
                    cost[y+dy][x+dx] = c
                    if not visited[y+dy][x+dx]:
                        heapq.heappush(heap, (c, (y+dy, x+dx)))
                    
print(cost[N-1][M-1])