import sys

input = sys.stdin.readline

N = int(input())
tmp = input().split()
nums = ["@"]
for c in tmp:
    nums.append(c)
    nums.append("@")
M = int(input())
len_nums = len(nums)

P = [0] * len_nums
r = 0
c = 0

for i in range(len_nums):
    if r < i:
        P[i] = 0
    else:
        P[i] = min(P[2*c - i], r-i)
        
    while (i - P[i] -1 >= 0 and i + P[i] + 1 < len_nums) and (nums[i - P[i] - 1] == nums[i + P[i] + 1]):
        P[i] += 1
    
    if r < i + P[i]:
        r = i + P[i]
        c = i
        
for _ in range(M):
    S, E = map(int, input().split())
    S, E = 2*(S-1) + 1, 2*(E-1) + 1
    mid = (S+E) // 2
    
    print(1 if mid - P[mid] <= S or mid + P[mid] >= E else 0)