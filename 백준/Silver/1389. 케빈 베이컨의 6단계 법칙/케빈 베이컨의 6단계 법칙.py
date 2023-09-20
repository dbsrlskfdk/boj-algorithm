N, M = map(int, input().split())
graph = [[0] * (N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(N):
    for j in range(N):
        if i != j and graph[i][j] == 0:
            graph[i][j] = float('inf')
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
cnt = []
for i in range(N):
    cnt.append(sum(graph[i]))
min_cnt = min(cnt)
for i in range(N):
    if cnt[i] == min_cnt:
        print(i+1)
        break