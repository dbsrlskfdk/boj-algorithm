from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b - 1].append(a - 1)

def bfs(t):
    visited = [False] * N
    que = deque([t])
    cnt = 1
    while que:
        v = que.popleft()
        visited[v] = True
        for nv in graph[v]:
            if not visited[nv]:
                que.append(nv)
                visited[nv] = True
                cnt += 1
    return cnt

max_cnt = -99999
ans = []
for i in range(N):
    count = bfs(i)
    if count > max_cnt:
        max_cnt = count
        ans = [i+1]
    elif count == max_cnt:
        ans.append(i+1)
print(*ans)