import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

L = 0
R = max(trees)
max_height = 0

while L <= R:
    mid = (L + R) // 2
    
    tmp_tree = 0
    
    for tree in trees:
        if tree > mid:
            tmp_tree += tree - mid
    
    if tmp_tree >= M:
        max_height = max(max_height, mid)
        L = mid + 1
    else:
        R = mid - 1
        
print(max_height)