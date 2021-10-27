N = int(input())
tri = [list(map(int, input().split(" "))) for _ in range(N)]


DP = [[0 for _ in range(N)] for _ in range(N)]
if N == 1:
    DP[0][0] = tri[0][0]
else:
    DP[0][0] = tri[0][0]
    DP[1][0] = tri[0][0] + tri[1][0]
    DP[1][1] = tri[0][0] + tri[1][1]
    
if N == 1:
    DP[0][0] = tri[0][0]
else:
    for i in range(1, N):
        for j in range(len(tri[i])):
            if j == 0:
                DP[i][j] = DP[i-1][j] + tri[i][j]
            elif j == len(tri[i])-1:
                DP[i][j] = DP[i-1][j-1] + tri[i][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + tri[i][j]    
                
print(max(DP[N-1]))                
