T = int(input())
dp = [[0 for _ in range(3+1)] for _ in range(10_001)]
dp[1][1] = 1 # 1
dp[2][1] = 1 # 1 + 1
dp[2][2] = 1 # 2
dp[3][1] = 1 # 1 + 1 + 1
dp[3][2] = 1 # 1 + 2
dp[3][3] = 1 # 3

for i in range(4, 10_001):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
    
for _ in range(T):
    n = int(input())
    print(sum(dp[n]))