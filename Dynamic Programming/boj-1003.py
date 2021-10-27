import sys

def fibonacci(n):
    tmp[0] = [1, 0]
    tmp[1] = [0, 1]
    for i in range(2, n+1):
        tmp[i][0] = tmp[i-1][0] + tmp[i-2][0]
        tmp[i][1] = tmp[i-1][1] + tmp[i-2][1]
    return tmp[n]

N = int(input())
num_list = []
tmp = []
for i in range(41):
    tmp.append([0,0])

for i in range(N):
    num_list.append(int(input()))

for i in range(N):
    fibonacci(num_list[i])
    sys.stdout.write(str(tmp[num_list[i]][0])+" ")
    sys.stdout.write(str(tmp[num_list[i]][1])+'\n')
