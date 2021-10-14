N = int(input())
wine = [int(input()) for i in range(N)]

sum = [0 for i in range(N+1)]
if N == 1:
    sum[0] = wine[0]
else:
    sum[0] = wine[0]
    sum[1] = max(wine[1], sum[0] + wine[1])
    for i in range(2, N):
        sum[i] = max(sum[i-1], sum[i-2] + wine[i])
        sum[i] = max(sum[i], sum[i-3] + wine[i-1] + wine[i])
print(sum[N-1])
