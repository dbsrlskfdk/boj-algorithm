N, K = map(int, input().split(" "))
nums = [int(input()) for _ in range(N)]

max_lan = max(nums)
L = 1
R = max_lan
answer = -1

while L <= R:
    mid = (L+R) // 2
    
    cnt = 0
    
    for i in range(N):
        cnt += nums[i] // mid
    
    if cnt < K:
        R = mid - 1
    else:
        L = mid + 1
        answer = max(answer, mid)
        
print(answer)