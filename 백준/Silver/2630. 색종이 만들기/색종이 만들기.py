N = int(input())
graphs = [list(map(int, input().split(" "))) for _ in range(N)]
cnt = [0, 0]

def rec_func(y, x, N):
    global cnt
    tmp = 0
    for i in range(y, y+N):
        for j in range(x, x+N):
           if graphs[i][j]:
               tmp += 1
    
    if tmp == 0:
        cnt[0] += 1
    elif tmp == N ** 2:
        cnt[1] += 1
    else:
        for i in range(2):
            for j in range(2):
                rec_func(y+i*N//2, x+j*N//2, N//2)
    
    return

rec_func(0, 0, N)

print(cnt[0])
print(cnt[1])