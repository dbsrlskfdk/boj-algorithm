N = int(input())
conection_list = [list(map(int, input().split(" "))) for i in range(N)]

conection_list.sort()

dp = [1 for i in range(N)]
for i in range(N):
    for j in range(0, i):
        if conection_list[i][1] > conection_list[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(N - max(dp))            
