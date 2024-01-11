sdoku = []
zero_idx = []
for i in range(9):
    tmp = []
    for j, v in enumerate(input()):
        tmp.append(int(v))
        if not int(v):
            zero_idx.append((i, j))
    
    sdoku.append(tmp)
    
def validate_sdoku(i, j, num):
    global sdoku
    # 행, 열 스도쿠  체크
    for k in range(9):
        if sdoku[i][k] == num: # 해당 행에 이미 들어있는 숫자면
            return False
        if sdoku[k][j] == num: # 해당 열에 이미 들어있는 숫자면
            return False
    
    # 스퀘어 스도쿠 체크
    st_row = (i // 3) * 3
    st_col = (j // 3) * 3
    
    for k in range(3):
        for l in range(3):
            if sdoku[st_row + k][st_col + l] == num: # 해당 숫자가 속한 3x3 스퀘어에 이미 있는 숫자면
                return False
            
    return True


def dfs(idx):
    global sdoku, zero_idx
    if idx == len(zero_idx):
        for row in sdoku:
            print(*row, sep="")
        exit(0)
    
    r, c = zero_idx[idx]
    for num in range(1, 10):
        if validate_sdoku(r, c, num):
            sdoku[r][c] = num
            dfs(idx+1)
            sdoku[r][c] = 0
            

dfs(0)