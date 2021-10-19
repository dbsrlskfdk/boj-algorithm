N, K = map(int, input().split(" "))
item_list = [list(map(int, input().split(" "))) for i in range(N)]

dp = [[0]*(K+1) for i in range(N)] # [weight_sum, value_sum]

for i in range(N):
    for j in range(K+1):
        if j - item_list[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_list[i][0]] + item_list[i][1])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N-1][K])            
