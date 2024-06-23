from collections import deque

wheels = [deque(input()) for _ in range(4)]

for _ in range(int(input())): # [wheel_num, direction] 
    n, direction = map(int, input().split())


    n = n - 1

    base_wheel = [0, 0, 0, 0]
    base_wheel[n] = direction
    for i in range(n, 3):
        r, l = wheels[i][2], wheels[i][6]
        n_r, n_l = wheels[i+1][2], wheels[i+1][6]

        if r == n_l:
            continue
        else:
            base_wheel[i+1] = -1 * base_wheel[i]

    for i in range(n, 0, -1):
        r, l = wheels[i][2], wheels[i][6]
        n_r, n_l = wheels[i-1][2], wheels[i-1][6]

        if l == n_r:
            continue
        else:
            base_wheel[i-1] = -1 * base_wheel[i]

    
    for i, v in enumerate(base_wheel):
        wheels[i].rotate(v)
        
score = [2 ** int(i) if wheels[i][0] == '1' else 0 for i in range(4) ]
print(sum(score))