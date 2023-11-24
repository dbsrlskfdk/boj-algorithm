from collections import deque

def solution(rc, operations):
    answer = []
    row_n = len(rc)
    col_n = len(rc[0])    
    
    row = deque([deque(rc[i][1:col_n-1]) for i in range(row_n)])
    col_left = deque([rc[i][0] for i in range(row_n)])
    col_right = deque([rc[i][-1] for i in range(row_n)])
    
    for op in operations:
        if op == "ShiftRow":
            row.rotate(1)
            col_left.rotate(1)
            col_right.rotate(1)
        elif op == "Rotate":
            row[0].appendleft(col_left.popleft())
            col_right.appendleft(row[0].pop())
            row[-1].append(col_right.pop())
            col_left.append(row[-1].popleft())
            
    for i in range(row_n):
        answer.append([col_left[i]] + list(row[i]) + [col_right[i]])
    return answer