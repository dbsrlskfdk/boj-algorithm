import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
LIS = [-float('inf')]
ans = 0
for i in range(N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
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

print(ans)