from collections import deque, defaultdict

N, M = map(int, input().split())
gt_vertex = defaultdict(list)
lt_vertex = defaultdict(list)
gt_nums = [0] * (N+1)
lt_nums = [0] * (N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    gt_vertex[b].append(a)
    lt_vertex[a].append(b)
    
for i in range(1, N+1):
    visited = [0] * (N+1)
    gt_que = deque([i])
    while gt_que:
        v = gt_que.popleft()
        if visited[v]:
            continue
        visited[v] = 1
        gt_nums[i] += 1
        gt_que.extend(gt_vertex[v])
    gt_nums[i] -= 1
    
for i in range(1, N+1):
    visited = [0] * (N+1)
    lt_que = deque([i])
    while lt_que:
        v = lt_que.popleft()
        if visited[v]:
            continue
        visited[v] = 1
        lt_nums[i] += 1
        lt_que.extend(lt_vertex[v])
    lt_nums[i] -= 1
    
for i in range(1, N+1):
    if (gt_nums[i] > N // 2) or (lt_nums[i] > N // 2):
        cnt += 1

print(cnt)