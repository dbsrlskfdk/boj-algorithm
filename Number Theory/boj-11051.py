N, K = map(int, input().split(" ")) # Combination(N, K) 구하기

bin = [[0 for _ in range(N+1)] for _ in range(N+1)]
bin[0][0] = 1
bin[1][0] = 1
bin[1][1] = 1

for i in range(2, N+1):
    for j in range(0, i+1):
        if j == 0 or j == i:
            bin[i][j] = 1
        else:
            bin[i][j] = (bin[i-1][j-1] + bin[i-1][j]) % 10007
        # print(f'bin[{i}][{j}] = {bin[i][j]}')
        
print(bin[N][K])        
