import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
chicken_cnt = 0
chicken = []
house = []
city = [list(map(int, input().split(" "))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
            chicken_cnt += 1
            
chicken_check = [False for _ in range(chicken_cnt)]
min_sum = 999999
select_chicken_idx = [0 for _ in range(M)]

def f(k, n_chicken, house, chicken):
    global min_sum
    if k == M:
        inner_sum = 0
        for item in house:
            tmp_min_sum = 9999999
            for chick_idx in select_chicken_idx:
                tmp_min_sum = min(tmp_min_sum, abs(item[0]-chicken[chick_idx][0])+abs(item[1]-chicken[chick_idx][1]))
            inner_sum += tmp_min_sum
        min_sum = min(inner_sum, min_sum)
        return


    for i in range(select_chicken_idx[k-1], n_chicken):
        if not chicken_check[i]:
            select_chicken_idx[k] = i
            chicken_check[i] = True
            f(k+1, n_chicken, house, chicken)
            chicken_check[i] = False

f(0, chicken_cnt, house, chicken)
print(min_sum)