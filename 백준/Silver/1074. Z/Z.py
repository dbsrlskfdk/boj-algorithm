N, r, c = map(int, input().split())
def rec_func(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*rec_func(N-1, int(r/2), int(c/2))
print(rec_func(N, r, c))