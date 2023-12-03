from collections import deque, defaultdict

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = defaultdict(str)
    que = deque([(A, "")])
    visited[A] = ""
    
    while que:
        num, cmd = que.popleft()
        
        # D
        D = (num * 2) % 10000
        if 0 <= D < 10000 and not visited[D]:
            visited[D] = cmd + "D"
            que.append((D, cmd+"D"))     
        if D == B:
            break
            
        # S
        S = num - 1 if num != 0 else 9999
        if 0 <= S < 10000 and not visited[S]:
            visited[S] = cmd +"S"
            que.append((S, cmd+"S"))                
        if S == B:
            break
            
        # L
        L = str(num).zfill(4)
        L = int(L[1:] + L[0])
        if 0 <= L < 10000 and not visited[L]:
            visited[L] = cmd + "L"
            que.append((L, cmd+"L"))
        if L == B:
            break
            
        # R
        R = str(num).zfill(4)
        R = int(R[-1] + R[:-1])
        if 0 <= R < 10000 and not visited[R]:
            visited[R] = cmd + "R"
            que.append((R, cmd+"R"))
        if R == B:
            break
            
    print(visited[B])