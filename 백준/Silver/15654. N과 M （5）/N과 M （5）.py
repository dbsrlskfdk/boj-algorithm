N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(i, M, nums, arr, visited):
    if i == M:
        print(*arr)
        return
    
    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dfs(i+1, M, nums, arr+[nums[j]], visited)
            visited[j] = False
            
dfs(0, M, nums, [], [False]*N)