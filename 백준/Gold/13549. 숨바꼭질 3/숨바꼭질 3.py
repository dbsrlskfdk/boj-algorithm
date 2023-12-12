from collections import deque

N, K = map(int, input().split())

que = deque([N])
visited = [float('inf')] * (200_000+1)
visited[N] = 0

while que:
    v = que.popleft()
    
    if v == K:
        print(visited[v])
        break
    if 2 * v < 200_000+1 and visited[2*v] == float('inf'):
        visited[2*v] = visited[v]
        que.appendleft(2*v)
    if v - 1 >= 0 and visited[v-1] == float('inf'):
        visited[v-1] = visited[v] + 1
        que.append(v-1)
    if v + 1 < 200_000 + 1 and visited[v+1] == float('inf'):
        visited[v+1] = visited[v] + 1
        que.append(v+1)