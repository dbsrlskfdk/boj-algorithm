import sys

input = sys.stdin.readline

def custom_round(n):
    return int(n) + 1 if n-int(n) >= 0.5 else int(n)
    
n = int(input())
nums = [int(input()) for _ in range(n)]
cut_num = int(custom_round(n*0.15))

if n == 0:
    print(0)
elif cut_num == 0:
    print(int(custom_round(sum(nums) / n)))
else:
    print(int(custom_round(sum(sorted(nums)[cut_num:-cut_num])/(n-2*cut_num))))