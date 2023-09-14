N = int(input())
schedule = [list(map(int, input().strip().split(" "))) for _ in range(N)]
dp = [0] * (N+1)
prev_max = 0

for i in range(N):
	if i + schedule[i][0] < N+1:
		dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], dp[i] + schedule[i][1])
		prev_max = dp[i+schedule[i][0]]
		for j in range(i+schedule[i][0], N+1):
			dp[j] = max(prev_max, dp[j])
            
print(dp[-1])