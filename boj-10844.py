N = int(input())

# stair 은 100개까지 되기에, 그리고 끝자리 수는 0~9 가 가능하기에 초기화 해준다.
stair_num = [[0 for i in range(10 + 1)] for i in range(100+1)]

# N = 1, {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in range(1, 9+1):
    stair_num[1][i] = 1

# N = 2,
# ~0 : {10}
# ~1 : {21}
# ~2 : {12, 32}
# ~3 : {23, 43}
# ~4 : {34, 54}
# ~5 : {45, 65}
# ~6 : {56, 76}
# ~7 : {67, 87}
# ~8 : {78, 98}
# ~9 : {89}
for i in range(2, N+1):
    for j in range(0, 9 + 1):
        if j == 0:
            stair_num[i][j] += stair_num[i-1][j+1] # 1에서만 0으로 내려올 수 있다. 
        elif j == 9:
            stair_num[i][j] += stair_num[i-1][j-1] # 8에서만 9로 올라올 수 있다.
        else:
            stair_num[i][j] += stair_num[i-1][j-1] + stair_num[i-1][j+1] # 마지막 자릿수가 0이나 9가 아니라면, 양쪽에서 내려오고, 올라올 수 있다.

sum = 0
for i in range(0, 9+1):
    sum += stair_num[N][i]
    
print(sum%(10**9))    
