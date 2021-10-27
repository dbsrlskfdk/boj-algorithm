N, K = map(int, input().split(" "))

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1
  
print(int(factorial(N) / (factorial(N-K) * factorial(K))))  
