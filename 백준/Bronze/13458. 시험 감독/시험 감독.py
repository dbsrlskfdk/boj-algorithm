N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    A[i] -= B
    cnt += 1
    if A[i] <= 0:
        continue
    elif A[i] > 0:
        cnt += A[i] // C if A[i] % C == 0 else A[i] // C + 1
print(cnt)