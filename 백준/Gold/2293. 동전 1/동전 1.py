n, k = map(int, input().split(" "))
value = [int(input()) for _ in range(n)]
dp = [0] * 10001
dp[0] = 1
for v in value:
	for i in range(v, k+1):
		dp[i] += dp[i-v]
        
print(dp[k])