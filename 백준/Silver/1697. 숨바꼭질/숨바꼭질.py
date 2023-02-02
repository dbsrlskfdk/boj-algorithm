from collections import deque

N, K = map(int, input().split(" "))
graph = [0 for _ in range(100000 + 1)]
que = deque([N])

while que:
    t = que.popleft()
    
    tmp_N = [t-1, t+1, 2*t]
    
    for c in tmp_N:
        if  c >= 0 and c <= 100000:
            if graph[c] == 0 and c != N:
                graph[c] = graph[t] + 1
                que.append(c)
            
    if K in tmp_N:
        break
        
print(graph[K])