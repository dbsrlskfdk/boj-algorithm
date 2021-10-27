import sys

N = int(input())
stair_list =[]

for i in range(N):
    stair_list.append(int(input()))
    

sum = [0 for i in range(N)]
sum[0] = stair_list[0]
if N != 1: # N은 1인 케이스를 생각해야하기때문에
    sum[1] = max(sum[0]+stair_list[1], stair_list[1])
  
    for i in range(2, N):
        sum[i] = max(stair_list[i-1] + sum[i-3] + stair_list[i], sum[i-2] + stair_list[i])
    print(sum[N-1])
else:
    print(sum[0])    
