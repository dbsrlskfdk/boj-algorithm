from collections import Counter

N, K = map(int, input().split())
nums = list(map(int, input().split()))

i = 0
j = 0
max_len = 0
num_cnts = Counter()

while (i<N and j<N) and (i <= j):
    if num_cnts[nums[j]] < K:
        num_cnts[nums[j]] += 1
        max_len = max(max_len, j - i + 1)
        j += 1
    else:
        num_cnts[nums[i]] -= 1
        i += 1
print(max_len)