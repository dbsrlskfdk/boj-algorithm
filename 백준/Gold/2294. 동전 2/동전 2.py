n, k = map(int, input().split(" "))
coins = [int(input()) for _ in range(n)]

dp = [100001] * (k+1)
dp[0] = 0

for v in coins:
	for i in range(v, k+1):
		dp[i] = min(dp[i], i//v + dp[i%v], dp[i-v] + dp[v])

if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)