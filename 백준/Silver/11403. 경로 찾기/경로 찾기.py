N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = float('inf')
            
for i in range(N): # 경유 노드
    for j in range(N): # 출발 노드
        for k in range(N): # 도착 노드
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        else:
            graph[i][j] = 1
            
for i in range(N):
    print(*graph[i])