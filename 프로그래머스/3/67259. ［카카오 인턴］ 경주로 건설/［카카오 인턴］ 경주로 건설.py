from collections import deque

def solution(board):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    n = len(board[0])
    price_table = []
    for i in range(n):
        price_table.append([[float('inf')] * 4 if j==0 else None for j in board[i]])
    st = (0, 0)
    for i in range(4): price_table[0][0][i] = 0 
    
    que = deque([st])
    
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n and 0 <= nx < n) and board[ny][nx] == 0: # 범위에서 넘치지 않고, 벽이 아니라면
                for j in range(4):
                    if i == j or (y == 0 and x == 0):
                        if price_table[ny][nx][i] > price_table[y][x][i] + 100:
                            price_table[ny][nx][i] = price_table[y][x][i] + 100
                            que.append((ny, nx))
                    else:
                        if price_table[ny][nx][i] > price_table[y][x][j] + 600:
                            price_table[ny][nx][i] = price_table[y][x][j] + 600
                            que.append((ny, nx))
                                        
    return min(price_table[n-1][n-1])