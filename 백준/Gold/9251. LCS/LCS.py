C = input()
R = input()

def LCS(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0 for i in range(n+1)] for j in range(2)]

    bi = bool

    for i in range(m+1):
        bi = i & 1 # 비트연산.... i & 0000 0001 

        for j in range(n+1):
            if i==0 or j==0:
                L[bi][j] = 0
            elif X[i-1] == Y[j-1]:
                L[bi][j] = L[1-bi][j-1] + 1
            else:
                L[bi][j] = max(L[1-bi][j], L[bi][j-1])
    
    return L[bi][n]

print(LCS(C, R))