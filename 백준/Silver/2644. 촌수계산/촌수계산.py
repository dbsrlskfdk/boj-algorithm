from collections import defaultdict, deque

def bfs(i, graph, visited):
    que = deque([i])
    family = {}
    family[i] = 0
    while que:
        t = que.popleft()
        
        for node in graph[t]:
            if visited[node] == 0 and node != i:
                visited[node] = visited[t] + 1
                family[node] = visited[node]
                que.append(node)
    return family

n = int(input())
a, b = map(int, input().split(" "))
m = int(input())

conn = []
visited = [0 for _ in range(n+1)]
connection = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split(" "))
    conn.append([x, y])

for i in conn:
    p, q = i
    connection[p].append(q)
    connection[q].append(p)


family = bfs(a, connection, visited)

if b in family.keys():
    print(family[b] - family[a])
else:
    print(-1)