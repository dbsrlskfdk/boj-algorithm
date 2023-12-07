from collections import defaultdict

num_T = int(input())

def bellman_ford(st, N):
    INF = 2_000_000_000
    dist = [INF] * (N + 1)
    dist[st] = 0
    
    for i in range(N):
        for v in range(1, N+1):
            for t, e in graphs[v]:
                if dist[e] > dist[v] + t:
                    dist[e] = dist[v] + t
                    if i == N-1:
                        return True # 마지막까지 간선이 갱신되면 음의 사이클이 존재한다는 것
    
    return False

for _ in range(num_T):
    N, M, W = map(int, input().split())
    # 인접 리스트 활용
    graphs = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graphs[S].append((T, E))
        graphs[E].append((T, S))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graphs[S].append((-T, E))
    
    # graphs = []
    # for _ in range(M):
    #     S, E, T = map(int, input().split())
    #     graphs.append((S, E, T))
    # for _ in range(W):
    #     S, E, T = map(int, input().split())
    #     graphs.append((S, E, -T))
    
    if bellman_ford(1, N):
        print("YES")
    else:
        print("NO")
        