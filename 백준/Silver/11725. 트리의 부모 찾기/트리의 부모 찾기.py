from collections import defaultdict

N = int(input())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
stack = []
stack.append(1)
visited = defaultdict(bool)
visited[1] = True
tree_node = defaultdict(int)

while stack:
    v = stack.pop()
    for nv in tree[v]:
        if not visited[nv]:
            visited[nv] = True
            stack.append(nv)
            tree_node[nv] = v
            
for i in range(2, N+1):
    print(tree_node[i])