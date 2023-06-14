N, S = map(int, input().split())
num_list = list(map(int, input().split()))
st, ed = 0, 0
total_len = 100_000
total = num_list[0]

while st < N and ed < N:
	if total < S:
		if ed == N - 1:
			break
		ed += 1
		total += num_list[ed]
	else:
		total_len = min(total_len, ed - st + 1)
		total -= num_list[st]
		st += 1

if total_len == 100_000:
	total_len = 0
print(total_len)