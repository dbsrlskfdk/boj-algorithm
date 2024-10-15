N = int(input())
nums = list(map(int, input().split()))

stack = []
recv_top = []

for i in range(N):
    if not stack:
        recv_top.append(0)
        stack.append([i+1, nums[i]])
    elif stack[-1][1] > nums[i]: # stack의 top이 더 크면,
        recv_top.append(stack[-1][0])
        stack.append([i+1, nums[i]])
    elif stack[-1][1] < nums[i]: # stack의 top이 더 작으면,
        prev_top = stack.pop()
        # 1. stack의 top이 현재 num보다 큰 값이 나올 때까지 뽑아야함.
        while prev_top[1] < nums[i]:
            if stack: # stack에 값이 있다면,
                if stack[-1][1] < nums[i]:
                    prev_top = stack.pop()
                else:
                    prev_top = stack[-1]
                    continue
            else:
                prev_top = None
                break

            
        if prev_top is not None:
            recv_top.append(prev_top[0])
        else:
            recv_top.append(0)

        
        stack.append([i+1, nums[i]])

print(*recv_top)    