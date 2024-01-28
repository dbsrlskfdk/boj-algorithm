N, M = map(int, input().split())
memory = list(map(int, input().split()))
C = list(map(int, input().split()))

total_cost = sum(C)

dp = [[0] * (total_cost+1) for _ in range(N)]

flag = False
ans = 0
for i in range(N):
    for j in range(total_cost+1):
        if j - C[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i - 1][j - C[i]] + memory[i])
        dp[i][j] = max(dp[i][j], dp[i-1][j])

for i in range(total_cost+1):
    if dp[N-1][i] >= M:
        print(i)
        break