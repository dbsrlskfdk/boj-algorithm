n = int(input())
dp = [0] * (n+1)

for i in range(1, int(n**0.5)+1):
    dp[i**2] = 1
    
for i in range(2, n+1):
    min_cnt = float('inf')
    for j in range(1, int(i**0.5)+1):
        min_cnt = min(min_cnt, dp[j**2] + dp[i-j**2])
    dp[i] = min_cnt
    
print(dp[n])