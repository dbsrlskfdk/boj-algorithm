import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                continue
            else:
                graphs[i][j] += graphs[i][j-1]
        else:
            if j == 0:
                graphs[i][j] += graphs[i-1][j]
            else:
                graphs[i][j] = graphs[i][j] + graphs[i-1][j] + graphs[i][j-1] - graphs[i-1][j-1]
                
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    
    if x1 == 0 and y1 == 0:
        print(graphs[x2][y2])
    elif x1 == 0: # 만약 x1이 시작 위치라면, x2에 대해서 y1-1번째까지의 합을 빼주면 된다.
        print(graphs[x2][y2] - graphs[x2][y1-1])
    elif y1 == 0: # 만약 y1이 시작 위치라면, y2에 대해서 x1-1번째까지의 합을 빼주면 된다.
        print(graphs[x2][y2] - graphs[x1-1][y2])
    else: # 만약 일반적인 케이스라면, x1-1까지 와 y1-1까지의 합을 빼주고, 두개에서 중복으로 빠진 x1-1, y1-1까지의 합을 더해주면 된다.
        print(graphs[x2][y2] - graphs[x1-1][y2] - graphs[x2][y1-1] + graphs[x1-1][y1-1])