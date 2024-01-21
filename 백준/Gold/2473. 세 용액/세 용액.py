import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
nums_list = []

ans = float('inf')
for i in range(N-2):
    st = i+1
    ed = N-1
    while st < ed:
        if ans > abs(nums[i] + nums[st] + nums[ed]):
            ans = abs(nums[i] + nums[st] + nums[ed])
            nums_list = [nums[i], nums[st], nums[ed]]
        if nums[i] + nums[st] + nums[ed] < 0:
            st += 1
        else:
            ed -= 1
            
print(*nums_list)