import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [-float('inf')]
P = []
ans = 0
for i in range(N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
        P.append(ans)
        ans += 1
    else:
        st = 0
        ed = ans
        
        while st <= ed:
            mid = (st + ed) // 2
            
            if LIS[mid] == A[i]:
                st = mid
                break
                
            if LIS[mid] < A[i]:
                st = mid + 1
            else:
                ed = mid -1
        
        LIS[st] = A[i]
        P.append(st-1)
        
p_max = max(P)
print_que = []
for i in range(len(P)-1, -1, -1):
    if p_max == P[i]:
        print_que.append(A[i])
        p_max -= 1

print(ans)
print(*print_que[::-1])