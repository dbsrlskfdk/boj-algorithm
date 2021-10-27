N = int(input())
num_list = list(map(int, input().split(" ")))

dp = [0 for i in range(N)] # i번쨰 숫자까지의 연속합 중 최댓갑
dp[0] = num_list[0]

if N != 1:
    dp[1] = max(dp[0] + num_list[1], num_list[1])

    for i in range(2, N):
        dp[i] = max(dp[i-1] + num_list[i], num_list[i])
    print(max(dp))
else:
    print(dp[0])
