A = input()
B = input()
len_A = len(A)
len_B = len(B)

LCS = [[0] * (len_B+1) for _ in range(len_A+1)]
for i in range(len_A+1):
    for j in range(len_B+1):
        if i == 0 or j ==0:
            LCS[i][j] = 0
        elif A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            
res = []
i = len_A
j = len_B
while i and j:
    if LCS[i-1][j] == LCS[i][j]:
        i -= 1
        continue
    elif LCS[i][j-1] == LCS[i][j]:
        j -= 1
        continue
    else:
        i -= 1
        j -= 1
        res.append(A[i])
        
print(LCS[-1][-1])
print("".join(res[::-1]))