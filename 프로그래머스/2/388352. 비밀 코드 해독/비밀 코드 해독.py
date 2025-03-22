from itertools import combinations

def solution(n, q, ans):
    answer = 0
    combs = combinations(range(1, n+1), 5)
    
    for comb in combs:
        flag = True
        nums = set(comb)
        for q_nums, n_ans in zip(q, ans):
            if len(set(q_nums).intersection(nums)) != n_ans:
                flag = False
                break
        if flag:
            answer += 1
            
    return answer