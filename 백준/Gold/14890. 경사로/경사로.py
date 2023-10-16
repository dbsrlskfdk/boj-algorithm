N, L = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    placed = [False] * N
    prev_num = 0
    flag = False
    for j in range(N):
        if prev_num == 0:
            prev_num = map_list[i][j]
            continue
        if prev_num == map_list[i][j]:
            continue
        elif prev_num + 1 == map_list[i][j]: # 이전의 높이 < 현재의 높이 -> 오르막 계단 필요
            if j - L < 0: # 계단을 놓을 수 없는 경우
                flag = True
                break
            for k in range(j-1, j-L-1, -1): # 계단을 놓는다면, 이전 계단부터 L칸 전까지
                if map_list[i][k] != prev_num or placed[k]: # 이전 계단과 높이가 다르거나 이미 계단이 놓여있는 경우
                    flag = True
                    break
                placed[k] = True # 아니라면 계단을 놓기
            else: # 계단을 다 놓고 나서
                prev_num = map_list[i][j] # 현재 계단으로 지정
                continue
        elif prev_num - 1 == map_list[i][j]: # 이전의 높이 > 현재의 높이 -> 내리막 계단 필요
            if j + L > N: # 계단을 놓을 수 없는 경우
                flag = True
                break
            for k in range(j, j+L): # 계단을 놓는다면, 현재 계단부터 L칸 후까지
                if map_list[i][k] != map_list[i][j] or placed[k]: # 현재 계단과 높이가 다르거나 이미 계단이 놓여있는 경우
                    flag = True
                    break
                placed[k] = True # 아니라면 계단을 놓기
            else: # 계단을 다 놓고 나서
                prev_num = map_list[i][j+L-1] # 현재 계단으로 지정
                continue
        else: # 높이가 2 이상 차이나는 경우
            flag = True
            break
    
    if flag:
        continue
    else:
        cnt += 1
        
for i in range(N):
    placed = [False] * N
    prev_num = 0
    flag = False
    for j in range(N):
        if prev_num == 0:
            prev_num = map_list[j][i]
            continue
        if prev_num == map_list[j][i]:
            continue
        elif prev_num + 1 == map_list[j][i]: # 이전의 높이 < 현재의 높이 -> 오르막 계단 필요
            if j - L < 0: # 계단을 놓을 수 없는 경우
                flag = True
                break
            for k in range(j-1, j-L-1, -1): # 계단을 놓는다면, 이전 계단부터 L칸 전까지
                if map_list[k][i] != prev_num or placed[k]: # 이전 계단과 높이가 다르거나 이미 계단이 놓여있는 경우
                    flag = True
                    break
                placed[k] = True # 아니라면 계단을 놓기
            else: # 계단을 다 놓고 나서
                prev_num = map_list[j][i] # 현재 계단으로 지정
                continue
        elif prev_num - 1 == map_list[j][i]: # 이전의 높이 > 현재의 높이 -> 내리막 계단 필요
            if j + L > N: # 계단을 놓을 수 없는 경우
                flag = True
                break
            for k in range(j, j+L): # 계단을 놓는다면, 현재 계단부터 L칸 후까지
                if map_list[k][i] != map_list[j][i] or placed[k]: # 현재 계단과 높이가 다르거나 이미 계단이 놓여있는 경우
                    flag = True
                    break
                placed[k] = True # 아니라면 계단을 놓기
            else: # 계단을 다 놓고 나서
                prev_num = map_list[j+L-1][i] # 현재 계단으로 지정
                continue
        else: # 높이가 2 이상 차이나는 경우
            flag = True
            break
    
    if flag:
        continue
    else:
        cnt += 1
        
print(cnt)