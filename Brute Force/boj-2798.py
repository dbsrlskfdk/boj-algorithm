N, M = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))
sum_list = []
M_diff = 100000
for i in range(N):
    for j in range(N):
        if j != i:
            for t in range(N):
                if t != j and t != i:
                    sum = num_list[i] + num_list[j] + num_list[t]
                    if M_diff == 100000:
                        M_diff = sum-M
                    elif sum <= M and abs(sum-M) <= abs(M_diff):
                        M_diff = sum-M
print(M_diff + M)
