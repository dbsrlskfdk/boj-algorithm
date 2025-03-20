import sys

from collections import defaultdict

input = sys.stdin.readline

tree_cnts = defaultdict(int)
total = 0
while True:
    tree_name = input().strip()
    
    if tree_name:
        tree_cnts[tree_name] += 1
        total += 1
    else:
        for name, cnt in sorted(tree_cnts.items(), key=lambda x : x[0]):
            print(f"{name} {cnt/total*100:.4f}")
        break