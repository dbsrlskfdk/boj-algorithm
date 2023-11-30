#%%
from collections import defaultdict

N, M, B = map(int, input().split(" "))
graphs = [list(map(int, input().split(" "))) for _ in range(N)]
heights = defaultdict(int)
for i in range(N):
    for j in range(M):
        heights[graphs[i][j]] += 1

heights = {i : v for i,v in sorted(heights.items(), key=lambda x: x[1])}

R = 256
times = float('inf')
flattened = 0

for flatten_height in range(R+1):
    temp_b = B
    temp_time = 0
    for i in heights:
        if i < flatten_height: # 평탄화시킬 높이보다 낮다면
            diff_height = flatten_height - i
            temp_b -= diff_height * heights[i] # 추가할 양만큼 인벤토리에서 제거
            temp_time += diff_height * heights[i] * 1 # 제거한 양 * 1 만큼 시간이 듬
        elif i > flatten_height: # 평탄화시킬 높이보다 높다면
            diff_height = i - flatten_height 
            temp_b += diff_height * heights[i] # 제거한 양만큼 인벤토리에 추가
            temp_time += diff_height * heights[i] * 2 # 제거한 양 * 2 만큼 시간이 듬
    
    if temp_b >= 0: # 평탄화 높이가 가능하다면 -> 블럭이 남거나 딱 맞을 것
        if temp_time <= times: # 시간이 최소인걸 구해야하니까.. 만약 시간이 같으면, 높이가 가장 높은 것을 구해야하기에, 같을 떄도 비교해줘야함
            times = temp_time
            flattend = flatten_height   

print(times, flattend)