T = int(input())
num_list = [list(map(int, input().split(" "))) for i in range(T)]

def GCD(a, b):
    if a <= b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
      
for i in range(T):
    print(int(num_list[i][0] * num_list[i][1] / GCD(num_list[i][0], num_list[i][1])))      
