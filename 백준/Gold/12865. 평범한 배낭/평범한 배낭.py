N, K = map(int, input().split()) # 물건 갯수, 버틸 수 있는 최대 무게
stuff = [] # [무게, 가치]

for _ in range(N):
    stuff.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(N+1)] for _ in range(K+1)] #  # [버틸 수 있는 최대 무게, 물건 갯수]

# Knapsack Algorithm
for i in range(K+1): # 버틸 수 있는 최대 무게에서
    for j in range(N+1):
        if i == 0 or j == 0: # 버틸 수 있는 최대 무게가 0이거나, 0번째 물건의 가치까지는 0으로 초기화
            dp[i][j] = 0
        elif i < stuff[j-1][0]: # 만약 버틸 수 있는 최대 무게 < 현재 순회하는 물건의 무게보다 작다면
            dp[i][j] = dp[i][j-1] # 이전까지 버텼던 무게까지의 가치를 그대로 가져옴
        else: # 만약 버틸 수 있는 최대 무게 >= 현재 순회하는 물건의 무게라면
            dp[i][j] = max(dp[i][j-1], dp[i-stuff[j-1][0]][j-1] + stuff[j-1][1]) # 이전까지 버텼던 무게까지의 가치와, 현재 물건을 넣었을 때의 가치를 비교하여 더 큰 값을 가져옴            
print(dp[K][N])