N = int(input())
num_list = list(map(int, input().split(" ")))

dp = [1 for i in range(N)] # 어차피 모든 수는 수열에 자기 자신을 포함하기에, 1이 default 값이 될 것이다.
# dp : 자신보다 인덱스가 작은 곳부터 자신까지의 LIS
dp_2 = [1 for i in range(N)]
for i in range(0, N): # 첫번째 수부터 순환을 시작한다.
    for j in range(0, i): # 
        if num_list[i] > num_list[j]: # 만약 순환을 돌다가 자신보다 숫자가 작으면, 자신의 dp 보다 해당 숫자의 dp에 1을 더한(num_list[i]의 한 케이스를 늘려주는) 것 중 큰 것을 대입
            dp[i] = max(dp[i], dp[j]+1)  
for t in range(N-1, 0-1, -1):
    for u in range(N-1, t, -1):
        if num_list[t] > num_list[u]:
            dp_2[t] = max(dp_2[t], dp_2[u]+1)

dp_3 = [dp[i] + dp_2[i] -1 for i in range(N)]

print(max(dp_3))
