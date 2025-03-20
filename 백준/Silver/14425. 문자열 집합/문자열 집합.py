vocab_set = set()
cnt = 0
N, M = map(int, input().split(" "))
for _ in range(N):
    vocab_set.add(input())
for _ in range(M):
    if input() in vocab_set:
        cnt += 1
print(cnt)