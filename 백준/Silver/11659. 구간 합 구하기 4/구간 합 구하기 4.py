import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] * (N+1)
for i, v in enumerate(list(map(int, input().split()))):
	nums[i+1] = nums[i] + v if i != 0 else v
    
for _ in range(M):
	i, j = map(int, input().split())
	print(nums[j] - nums[i-1])