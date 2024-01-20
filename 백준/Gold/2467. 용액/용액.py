import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

st = 0
ed = N-1
ans = float('inf')
ans_list = []
while st < ed:
    if ans >= abs(nums[st] + nums[ed]):
        ans = abs(nums[st] + nums[ed])
        ans_list = [st, ed]
    if nums[st] + nums[ed] < 0:
        st += 1
    else:
        ed -= 1
        
print(nums[ans_list[0]], nums[ans_list[1]])