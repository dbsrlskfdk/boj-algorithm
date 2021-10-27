N, K = map(int, input().split(" "))
A = []

for i in range(N):
    A.append(int(input()))
    
coin_num = 0
for i in range(N-1, 0-1, -1):
    coin_num += (K // A[i])
    K %= A[i]    

print(coin_num)    
