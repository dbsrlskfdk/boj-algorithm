V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, (A, B)))
    
edges = sorted(edges, key=lambda x : x[0])
parents = [i for i in range(V+1)]

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
    
    
spanning_dist = 0
e_num = 0
for w, (a, b) in edges:
    if find(a) != find(b):
        spanning_dist += w
        e_num += 1
    
    union(a, b)
    
   # if e_num == V-1:
   #     break
        
print(spanning_dist)