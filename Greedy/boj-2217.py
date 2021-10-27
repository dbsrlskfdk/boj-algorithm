
N = int(input())
rope = [int(input()) for i in range(N)]

rope.sort()
ans = 0
for i in range(1, N+1):
    ans = max(ans, rope[N-i] * i)

print(ans)
