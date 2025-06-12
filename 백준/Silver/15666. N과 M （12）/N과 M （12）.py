N, M = map(int, input().split())
arrs = list(set((map(int, input().split()))))
arrs.sort()
real_N = len(arrs)


def dfs(prev_idx, prev, length):
    if length == M:
        print(" ".join(prev))
        return

    for i in range(prev_idx, real_N):
        dfs(i, prev + [str(arrs[i])], length + 1)


def solution():
    dfs(0, [], 0)


if __name__ == "__main__":
    solution()
