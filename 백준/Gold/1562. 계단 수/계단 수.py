N = int(input())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N)] 
for k in range(1, 10):
    dp[0][k][1<<k] = 1
    
for i in range(1, N):
    for k in range(10):
        for bit in range(1<<10):
            if k - 1 >= 0:
                dp[i][k][bit | (1 << k)] += dp[i - 1][k - 1][bit]
            if k + 1 <= 9:
                dp[i][k][bit | (1 << k)] += dp[i - 1][k + 1][bit]
            dp[i][k][bit | (1 << k)] %= 1_000_000_000
            
cnt = 0
for k in range(10):
    cnt += dp[N-1][k][1023]
    cnt %= 1_000_000_000
    
print(cnt)