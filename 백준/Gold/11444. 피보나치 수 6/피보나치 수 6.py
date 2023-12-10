from collections import defaultdict

n = int(input())
dp = defaultdict(int)

dp[0] = 0
dp[1] = 1
dp[2] = 1

def fibonacci(n):
    if not dp[n]:
        if n & 1: # 홀수면
            fn = fibonacci(n//2)
            fn_p1 = fibonacci(n//2 + 1)
            
            dp[n] = (fn ** 2 + fn_p1 ** 2) % 1_000_000_007
        else: # 짝수면
            fn = fibonacci(n//2)
            fn_m1 = fibonacci(n//2 - 1)
            
            dp[n] = (fn * (fn + 2 * fn_m1)) % 1_000_000_007
        
    return dp[n]

print(fibonacci(n))