import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(i, visited):
    if visited == (1 << N) - 1: # 모든 도시 방문했다면 1111...1(N개) - 1
        return costs[i][0] if costs[i][0] else float('inf') # 출발지(0)으로 방문하는 경로가 있다면, 비용을 반환 아니면 초기화값
    
    if dp[i][visited] != -1: # 최솟값 계산되어 있으면, 반환
        return dp[i][visited]
    
    ret = float('inf')
    for k in range(1, N): # 모든 도시 방문 체크
        if not costs[i][k] or visited & (1 << k): # i -> k로 가는 경로가 없으면, 혹은 이미 방문했으면
            continue
        
        ret = min(ret,
                 tsp(k, visited | (1 << k)) + costs[i][k])
    
    dp[i][visited] = ret
    return dp[i][visited]


print(tsp(0, 1))