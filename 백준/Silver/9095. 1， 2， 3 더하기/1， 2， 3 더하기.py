T = int(input())
dp = [0] * 11
    
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for _ in range(T):
    a = int(input())
    print(dp[a])