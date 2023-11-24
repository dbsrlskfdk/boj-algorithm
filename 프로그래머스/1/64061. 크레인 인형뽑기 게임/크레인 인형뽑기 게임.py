from collections import deque

def solution(board, moves):
    rows = [deque(board[j][i] for j in range(len(board[0]))) for i in range(len(board))]
    score = 0
    stack = []
    for i in moves:
        while rows[i-1]:
            cur = rows[i-1].popleft()
            if cur:
                break
        else:
            continue
        
        if stack:
            if stack[-1] == cur:
                stack.pop()
                score += 2
            else:
                stack.append(cur)
        else:
            stack.append(cur)
    
    return score