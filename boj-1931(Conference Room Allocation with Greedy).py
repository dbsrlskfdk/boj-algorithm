N = int(input())
conf = []

for i in range(N):
    conf.append(list(map(int, input().split(" "))))

# Greedy 알고리즘
# 명제를 찾아서, 이렇게 될 것이다 라는 확신을 갖고 알고리즘을 작성하는게 필요
# 시작 시간이 이전 Task가 끝나는 시간 이상인 스케쥴 중에, 끝나는 시간이 가장 빠른 Task를 수행해야지 가장 많은 Task를 수행할 것이다.
# 그렇기에, 끝나는 시간이 빠른 순으로 정렬을 하고, 같은 시간에 끝나는 Task에 대해서 일찍 시작하는 것을 수행해야 하기 때문에, 시작 시간이 빠른 것으로 또 정렬을 해준다.
# 끝나는 시간 빠른 순 정렬 -> 시작 시간 빠른 순 정렬(끝나는 시간이 같은 Task에 대해서)
# 근데 Python 은 그게 안됨.. 그래서 시작 시간 빠른 순으로 먼저 정렬을 해주고 나서, 끝나는 시간이 빠른 순으로 정렬해야지 위의 말처럼 수행된다.

conf.sort(key = lambda x : x[0])
conf.sort(key = lambda x : x[1])

cnt = 0
end = 0
for i in range(N):
    if end > conf[i][0]:
        continue
    cnt += 1
    end = conf[i][1]
print(cnt)    

#=========================================================
# O(N^2) 의 시간복잡도를 갖는 알고리즘.. 모든 케이스를 다 수행해서 체크하는건데 시간초과 남
end = 0
cnt = 0
tmp_cnt = 0
for i in range(N):
    end = conf[i][1]
    tmp_cnt = 1
    print(f'start_time : {conf[i][0]}, end_time : {end}')
    for j in range(N):
        if i != j:
            if end <= conf[j][0]:
                tmp_cnt += 1
                end = conf[j][1]
                print(f'start_time : {conf[j][0]}, end_time : {end}')
                continue
    print("=================================")
    print(f'cnt = {tmp_cnt}')
    cnt = max(tmp_cnt, cnt)
print(cnt)   
