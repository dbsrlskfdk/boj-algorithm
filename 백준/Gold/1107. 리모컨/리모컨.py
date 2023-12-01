import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
unable_buttons = list(map(int, input().strip().split(" "))) if M != 0 else []

n_push = abs(N - 100)

for num in range(1_000_001):
    num = str(num)
    
    for j in range(len(num)):
        if int(num[j]) in unable_buttons:
            break
        elif j == len(num) - 1:
            n_push = min(n_push, abs(int(num) - N) + len(num))
            
print(n_push)