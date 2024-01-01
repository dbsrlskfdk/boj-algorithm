import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, (u, v)))
    
edges = sorted(edges, key=lambda x : x[0])
parents = [i for i in range(N+1)]

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
# max_edges = 0
for w, (a, b), in edges:
    if e_num == N-2:
        break
        
    if find(a) != find(b):
        spanning_dist += w
        # max_edges = max(max_edges, w)
        e_num += 1
    
    union(a, b)
    
    
        
print(spanning_dist)