num = [0 for i in range(101)]
def dp(n):
    if n == 1 or n == 2 or n == 3:
        num[n] = 1
        return 1
    elif num[n] != 0:
        return num[n]
    num[n] = dp(n-2) + dp(n-3)

    return num[n]

T = int(input())
for i in range(T):
    N = int(input())
    print(dp(N))
