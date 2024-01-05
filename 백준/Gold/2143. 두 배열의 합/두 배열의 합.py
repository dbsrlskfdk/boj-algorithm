from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))
A_sum = [0] * n
A_sum[0] = A[0]
for i in range(1, n):
    A_sum[i] = A[i] + A_sum[i-1]
    
m = int(input())
B = list(map(int, input().split()))
B_sum = [0] * m
B_sum[0] = B[0]
for i in range(1, m):
    B_sum[i] = B[i] + B_sum[i-1]
    
A_sub = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        A_sub[A_sum[j] - A_sum[i-1] if i != 0 else A_sum[j]] += 1
        
B_sub = defaultdict(int)
for i in range(m):
    for j in range(i, m):
        B_sub[B_sum[j] - B_sum[i-1] if i != 0 else B_sum[j]] += 1
        
A_sub_sort = sorted(A_sub)
B_sub_sort = sorted(B_sub, reverse=True)

a, b = 0, 0
cnt = 0
flag = False # True면 b가 증가, False면 a가 증가

while a < len(A_sub) and b < len(B_sub):
    # print(a, b)
    # print(f"{A_sub[a]=}, {B_sub[b]=}")
    section_sum = A_sub_sort[a] + B_sub_sort[b]
    
    if section_sum > T:
        b += 1
        flag = True
    elif section_sum < T:
        a += 1
        flag = False
    else:
        cnt += A_sub[A_sub_sort[a]] * B_sub[B_sub_sort[b]]
        # 같을 떄 처리를 어떻게 할건지...
        if flag:
            a += 1
        else:
            b += 1
            
print(cnt)