N = int(input())

for i in range(N+1):
    tmp_sum = 0
    if i < 10:
        tmp_sum = 2*i
    else:
        i = str(i)
        tmp_sum = sum([int(a) for a in i]) + int(i)

    if tmp_sum == N:
        print(int(i))
        break;
    elif int(i) == N and tmp_sum != N:
        print(0)
        break;
