from collections import defaultdict

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    len_W = len(W)
    min_len = 10_001
    max_len = 0


    char_cnts = defaultdict(list)
    for i, c in enumerate(W):
        char_cnts[c].append(i)
    
    
    for c, char_index in char_cnts.items():
        if len(char_index) < K:
            continue

        for i in range(len(char_index) - K + 1):
            min_len = min(min_len, char_index[i + K - 1] - char_index[i] + 1)
            max_len = max(max_len, char_index[i + K - 1] - char_index[i] + 1)

    if min_len != 10_001 and max_len != 0:
        print(min_len, max_len)
    else:
        print(-1)