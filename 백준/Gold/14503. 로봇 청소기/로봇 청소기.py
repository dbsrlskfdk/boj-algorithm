N, M = map(int, input().split(" "))
i, j, d = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]
cnt = 0
while True:
    if graph[i][j] == 0:
        cnt += 1
        graph[i][j] = 2
    # 4방향이 모두 벽일 때
        
    if graph[i-1][j] != 0 and graph[i+1][j] != 0 and graph[i][j-1] != 0 and graph[i][j+1] != 0:
        if d == 0: #바라보는 방향이 북쪽
            i += 1
        elif d == 1: #바라보는 방향이 동쪽
            j -= 1
        elif d == 2: #바라보는 방향이 남쪽
            i -= 1
        elif d == 3: #바라보는 방향이 서쪽
            j += 1

        if graph[i][j] == 1:
            break
        else:
            continue
    # 빈칸이 있을 때    
    else:
        # 반시계 방향으로 회전
        if d - 1 < 0:
            d = 3
        else:
            d -= 1
            
        if d == 0: #바라보는 방향이 북쪽
            if graph[i-1][j] == 0:
                i -= 1
        elif d == 1: #바라보는 방향이 동쪽
            if graph[i][j+1] == 0:
                j += 1
        elif d == 2: #바라보는 방향이 남쪽
            if graph[i+1][j] == 0:
                i += 1
        elif d == 3: #바라보는 방향이 서쪽
            if graph[i][j-1] == 0:
                j -= 1
                
print(cnt)                