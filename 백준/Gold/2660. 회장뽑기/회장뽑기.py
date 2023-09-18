N = int(input())
graph = [[0]*N for _ in range(N)]
dist_list = []
candidates = []
cnt = 0
i, j = map(int, input().split())

while i!=-1 and j!=-1:
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1
    i, j = map(int, input().split())
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0 and i!=j:
            graph[i][j] = float('inf')

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
    
for i in range(N):
    dist_list.append(max(graph[i]))

min_dist = min(dist_list)
for i in range(N):
    if dist_list[i] == min_dist:
        candidates.append(i+1)
        cnt += 1

print(min_dist, cnt)
print(*sorted(candidates))