N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
truth_num, *truth = map(int, input().split())
cnt = 0

party_list = []
for _ in range(M):
    attn_num, *attn = list(map(int, input().split()))
    party_list.append(attn)
    for i in range(attn_num):
        for j in range(attn_num):
            graph[attn[i]][attn[j]] = 1
            graph[attn[j]][attn[i]] = 1
            
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                graph[j][i] = 1
                
for party in party_list:
    flag = True
    for a in party:
        for b in truth:
            if graph[a][b]:
                flag = False
                break
        if not flag:
            break
    if flag:
        cnt += 1
        
print(cnt)