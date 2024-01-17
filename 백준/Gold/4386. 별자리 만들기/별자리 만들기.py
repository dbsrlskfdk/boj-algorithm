n = int(input())
coords = []
edges = []
for _ in range(n):
    a, b = map(float, input().split())
    coords.append((a, b))
    
for i in range(n):
    for j in range(i+1, n):
        w = ((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2) ** 0.5
        edges.append((w, (i, j)))
        
edges = sorted(edges, key=lambda x : x[0])
parents = [i for i in range(n)]

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    parents[y] = x
    
    
dist = 0
e_num = 0
for w, (a, b) in edges:
    if e_num == n-1:
        break
    
    if find(a) != find(b):
        dist += w
        e_num += 1
    
    union(a, b)

print(f"{dist:.2f}")