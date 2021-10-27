N = int(input())

DP = [[0, 0, 0]  for _ in range(N)]
a = [list(map(int, input().split(" "))) for i in range(N)]

for i in range(N):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + a[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + a[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + a[i][2]

print(min(DP[N-1][0], DP[N-1][1], DP[N-1][2]))

# 사실 이 작성법이 직관적이지는 않은거같다.
# DP[0][0] = a[0][0]
# DP[0][1] = a[0][1]
# DP[0][2] = a[0][2]
# 같이 처음 비용은 정의해주고, 뒤 과정을 진행해주는게 눈에 확 들어오는 작성법같다..
# DP를 0으로 초기화하고 진행하였기때문에, DP[i-1]의 최솟값이 0이기에 i=0일시에 값이 위의 작성법처럼 초초기화고 시작하지만, 한눈에 들어오는 느낌은 아니다.
