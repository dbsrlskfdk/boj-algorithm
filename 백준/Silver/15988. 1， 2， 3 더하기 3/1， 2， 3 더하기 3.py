import sys

input = sys.stdin.readline

T = int(input())
dp = [0] * 1_000_001
dp[0] = 1
dp[1] = 1
dp[2] = dp[0] + dp[1] # 1 + 1, 2

for i in range(3, 1_000_001):
    dp[i] += dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= 1_000_000_009
    
for _ in range(T):
    n = int(input())
    print(dp[n])