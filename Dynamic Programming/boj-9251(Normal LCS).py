C = input()
R = input()

LENGTH = [[0 for i in range(len(C) + 1)] for i in range(len(R) + 1)]

def LCS_Length(C, R):
    for i in range(1, len(R)+1):
        for j in range(1, len(C)+1):
            if C[j-1] == R[i-1]:
                LENGTH[i][j] = LENGTH[i-1][j-1] + 1
            else:
                LENGTH[i][j] = max(LENGTH[i][j-1], LENGTH[i-1][j])
    return LENGTH[len(R)][len(C)]

print(LCS_Length(C, R))
