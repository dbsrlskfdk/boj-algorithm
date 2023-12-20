from collections import defaultdict, deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_times = list(map(int, input().split()))
    
    graphs = defaultdict(list)
    build_orders = defaultdict(int)
    for _ in range(K):
        a, b = map(int, input().split())
        build_orders[b] += 1
        graphs[a].append((b, build_times[a-1]))
    winning_building = int(input())
    
    que = deque([])
    dp = [0] * (N+1)
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not build_orders[i]:
            que.append(i)

    while que:
        v = que.popleft()
        

        for nv, nw in graphs[v]:
            if dp[nv] < dp[v] + nw:
                dp[nv] = dp[v] + nw
            build_orders[nv] -= 1
            if build_orders[nv] == 0:
                que.append(nv)
                    
    print(dp[winning_building] + build_times[winning_building-1])