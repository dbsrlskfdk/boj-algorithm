N = int(input())
round_list = list(map(int, input().split(" ")))

def GCD(a, b):
    if a <= b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
      
for i in range(1, N):
    tmp = GCD(round_list[0], round_list[i])
    if tmp == 1:
        print(f'{round_list[0]}/{round_list[i]}')
    else:
        print(f'{round_list[0] // tmp}/{round_list[i] // tmp}')      
