def func(cur):
    global cnt
    if cur == N:
        cnt += 1
        return
    for i in range(N):
        if isused_y[i] or isused_x_pl_y[i+cur] or isused_x_mi_y[cur-i+N-1]:
            continue
        isused_y[i] = True
        isused_x_pl_y[i+cur] = True
        isused_x_mi_y[cur-i+N-1] = True
        func(cur+1)
        isused_y[i] = False
        isused_x_pl_y[i+cur] = False
        isused_x_mi_y[cur-i+N-1] = False

N = int(input())
cnt = 0
isused_y = [False] * N
isused_x_pl_y = [False] * (2*N-1)
isused_x_mi_y = [False] * (2*N-1)

func(0)
print(cnt)