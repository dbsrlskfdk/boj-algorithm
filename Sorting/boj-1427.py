N = list(input())
new_num = ''

for _ in range(len(N)):
    for i in range(len(N) - 1):
        if int(N[i]) < int(N[i+1]):
            tmp = N[i]
            N[i] = N[i+1]
            N[i+1] = tmp
new_num = new_num.join(N)
print(new_num)
