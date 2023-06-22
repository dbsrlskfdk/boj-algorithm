N, M = map(int, input().split())
A = list(map(int, input().split()))
st, ed = 0, 0
num = 0
total = A[ed]

while st < N and ed < N:
	if total < M:
		if ed + 1 < N:
			ed += 1
			total += A[ed]
		else:
			total -= A[st]
			st += 1
	elif total > M:
		total -= A[st]
		st += 1
	else:
		num += 1
		total -= A[st]
		st += 1
print(num)