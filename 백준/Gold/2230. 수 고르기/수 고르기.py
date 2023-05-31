N, M = map(int, input().split())
num_list = [int(input()) for _ in range(N)]
num_list.sort()

st, ed = 0, 0
last = 2_000_000_000

while st < N and ed < N :
	if num_list[ed] - num_list[st] < M:
		ed += 1
	else:
		last = min(num_list[ed] - num_list[st], last)
		if st < ed:
			st += 1
		else:
			ed += 1
            
print(last)