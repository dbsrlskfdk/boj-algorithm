n = int(input())
m = int(input())

dist = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(c, dist[a-1][b-1])
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
            
for i in dist:
    for j in i:
        if j == float('inf'):
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()