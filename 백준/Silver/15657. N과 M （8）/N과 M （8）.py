N, M = map(int ,input().split())
nums = list(map(int, input().split()))
nums.sort()

def dfs(i, st, visited, arr):
    if i == M:
        print(*arr)
        return
    
    for n in range(st, N):
        dfs(i+1, n, visited, arr+[nums[n]])
        
dfs(0, 0, [False]*(N+1), [])