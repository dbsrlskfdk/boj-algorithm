from collections import deque

def solution(land):
    num_rows = len(land)
    num_cols = len(land[0])
    
    col_cnt = [0 for _ in range(num_cols)]
    visited = set()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for i in range(num_rows):
        for j in range(num_cols):
            if (i, j) not in visited and land[i][j]:
                    que = deque([(i, j)])
                    visited.add((i, j))
                    col_has = set([j])
                    cnt = 1
                    while que:
                        y, x = que.popleft()
                        
                        for h in range(4):
                            ny = y + dy[h]
                            nx = x + dx[h]
                        
                            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                                if (ny, nx) not in visited and land[ny][nx]:
                                    cnt += 1
                                    col_has.add(nx)
                                
                                    que.append((ny, nx))
                                    visited.add((ny, nx))
                            
                    for c in col_has:
                        col_cnt[c] += cnt
    
    max_cnt = max(col_cnt)

    answer = max_cnt       
    return answer