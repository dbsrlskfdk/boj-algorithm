import math

N = int(input())
dp = [i for i in range(0, N+1)]
dp[1] = 0
num_list = []
for i in range(2, math.ceil(math.sqrt(N+1))):
	if dp[i] == 0:
		continue
	for j in range(2*i, N+1, i):
		dp[j] = 0
for p in range(N+1):
	if dp[p] != 0:
		num_list.append(dp[p])
        
st, ed = 0, 0
total = num_list[0] if N != 1 else 0
num = 0

while st<len(num_list) and ed<len(num_list) and N != 1:
	if total == N:
		num += 1
		total -= num_list[st]
		st += 1
	elif total < N:
		ed += 1
		if ed < len(num_list):
			total += num_list[ed]
	else:
		total -= num_list[st]
		st += 1

print(num)