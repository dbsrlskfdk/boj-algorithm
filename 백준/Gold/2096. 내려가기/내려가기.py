import sys

input = sys.stdin.readline

N = int(input())

max_score = 0
min_score = 0
max_floor_sum = [0, 0, 0]
min_floor_sum = [0, 0, 0]
for i in range(0, N):
    nums = list(map(int, input().split()))
    
    max_tmp = [0, 0, 0]
    min_tmp = [0, 0, 0]
    
    max_tmp[0] = max(max_floor_sum[0] + nums[0],
                 max_floor_sum[1] + nums[0])
    
    max_tmp[1] = max(max_floor_sum[0] + nums[1],
                 max_floor_sum[1] + nums[1],
                 max_floor_sum[2] + nums[1])
    
    max_tmp[2] = max(max_floor_sum[2] + nums[2], 
                 max_floor_sum[1] + nums[2])
    
    min_tmp[0] = min(min_floor_sum[0] + nums[0],
                    min_floor_sum[1] + nums[0])
    
    min_tmp[1] = min(min_floor_sum[0] + nums[1],
                 min_floor_sum[1] + nums[1],
                 min_floor_sum[2] + nums[1])
    
    min_tmp[2] = min(min_floor_sum[2] + nums[2], 
                 min_floor_sum[1] + nums[2])
    
    max_floor_sum = max_tmp
    min_floor_sum = min_tmp
    
max_score = max(max_floor_sum)
min_score = min(min_floor_sum)
print(max_score, min_score)