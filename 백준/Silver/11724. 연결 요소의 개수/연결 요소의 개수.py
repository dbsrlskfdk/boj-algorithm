from collections import defaultdict

def dfs(graph):
    visited = [False] * (N+1)
    cnt = 0
    
    for v in graph.keys():
        if visited[v] == True:
            continue
        stack = [v]
    
        while stack:
            v = stack.pop()
            
            if visited[v] == False:
                visited[v] = True
                stack.extend(graph[v])
        else:
            cnt += 1
    return cnt

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges_dict = defaultdict(list)
for v in range(1, N+1):
    edges_dict[v] = []
for st_v, ed_v in edges:
    edges_dict[st_v].append(ed_v)
    edges_dict[ed_v].append(st_v)
    
print(dfs(edges_dict))