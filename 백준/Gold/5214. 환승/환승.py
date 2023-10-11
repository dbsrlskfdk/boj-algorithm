from collections import defaultdict, deque

N, K, M = map(int, input().split())
graph = defaultdict(list)
for n in range(1, M+1):
    hypertube = list(map(int, input().split()))
    for i in hypertube:
        graph[i].append(N+n)
        graph[N+n].append(i)
        
distance = [0] * (N+M+1)
que = deque([1])
distance[1] = 1

while que:
    cur = que.popleft()
    for i in graph[cur]:
        if distance[i] != 0:
            continue
        que.append(i)
        if i > N:
            distance[i] = distance[cur]
        else:
            distance[i] = distance[cur] + 1

if distance[N] != 0:
    print(distance[N])
else:
    print(-1)