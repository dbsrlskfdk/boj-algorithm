N = list(map(int, input().split()))
len_N = len(N)
steps = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(len_N)] # (len_N, 5, 5)
steps[0][0][0] = 0

def calc_distance(a, b): # a부터 b까지의 거리
    if a == 0: # 중앙에서 다른데로 움직이면 무조건 2의 힘
        return 2
    elif a == b: # 둘이 같은 위치로 움직이면 1의 힘
        return 1
    elif abs(b - a) == 2: # 반대편의 위치러 움직이면 4의 힘
        return 4
    else: # 그 외 인접한 지역은 3의 힘
        return 3
    
    
for i, v in enumerate(N):
    if not v:
        break
    
    # 전체 케이스에 대해서 움직임 힘 최솟값 계산
    for l in range(5):
        for r in range(5):
            steps[i+1][l][v] = min(steps[i+1][l][v],
                                   steps[i][l][r] + calc_distance(r, v)) # 왼쪽발은 가만히 있고, 오른쪽 발이 이동할 때
            
            steps[i+1][v][r] = min(steps[i+1][v][r],
                                   steps[i][l][r] + calc_distance(l, v)) # 오른쪽발은 가만히 있고, 왼쪽 발이 이동할 때
            
min_step = min([min(step) for step in steps[-1]])
print(min_step)