from collections import Counter
from itertools import combinations
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    mbti = input().split()
    mbti_cnt = Counter(mbti)
    cnt = float('inf')
    
    # mbti 갯수 체크 -> 2개가 넘어가면, 이미 그냥 그 3개 고르는게 최소 케이스니까
    mbti = []
    for m, v in mbti_cnt.items():
        if v < 3:
            mbti += [m] * v
        elif v >= 3:
            mbti += [m] * 3
    
    for comb in combinations(mbti, 3):
        tmp_cnt = 0
        for j in range(3):
            for i in range(4):
                if comb[j][i] != comb[(j+1) % 3][i]:
                    tmp_cnt += 1
        cnt = cnt if cnt < tmp_cnt else tmp_cnt
    
    print(cnt)