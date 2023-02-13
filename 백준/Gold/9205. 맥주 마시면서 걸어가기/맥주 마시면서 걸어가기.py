from collections import deque, defaultdict

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    graph = {i:list(map(int, input().split(" "))) for i in range(n+2)}
#     a = list(graph.values())[1:-1]
#     a.sort(key=lambda x : x[0],reverse=True)
#     for v, i in enumerate(range(1,n+1)):
#         graph[i] = a[v]
    edge = defaultdict(list)
    for i in range(n+2):
        for j in range(n+2):
            if i != j and (abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1])) / 50 <= 20:
                edge[i].append(j)
    visited = {i:False for i in range(n+2)}
    que = deque(edge[0])
    visited[0] = True

    while que:
        node = que.popleft()
        aft_x, aft_y = graph[node]
        if not visited[node]:
            que.extend(edge[node])
            visited[node] = True
            
            if visited[n+1]:
                answer.append('happy')
                break
    else:
        answer.append('sad')
        
for c in answer:
    print(c)        