from collections import defaultdict, deque

N, M = map(int, input().split())
graphs = defaultdict(list)
orders = defaultdict(int)

for _ in range(M):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        graphs[tmp[i]].append(tmp[i+1])
        orders[tmp[i+1]] += 1
        
que = deque()
for i in range(1, N+1):
    if not orders[i]:
        que.append(i)
        
print_que = []
print_len = 0
while que:
    v = que.popleft()
    
    print_que.append(v)
    print_len += 1
    for nv in graphs[v]:
        orders[nv] -= 1
        
        if not orders[nv]:
            que.append(nv)
            
if print_len == N:
    for i in print_que:
        print(i)
else:
    print(0)