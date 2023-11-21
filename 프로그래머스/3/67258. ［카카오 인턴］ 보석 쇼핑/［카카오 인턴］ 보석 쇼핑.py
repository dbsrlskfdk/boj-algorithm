from collections import defaultdict

def solution(gems):
    gems_sort_len = len(set(gems))
    end = 0
    tmp_list = defaultdict(int)
    tmp_sort = set()
    answer = []
    len_gems = len(gems)
    for st in range(len_gems):
        while len(tmp_sort) != gems_sort_len and end < len_gems:        
            tmp_list[gems[end]] += 1
            tmp_sort.add(gems[end])
            end += 1
        
        if len(tmp_sort) == gems_sort_len:
            if answer: 
                if abs(answer[-1][1] - answer[-1][0]) > abs((st+1) - end): # 원래 있던게 거리가 더 크면
                    answer.pop() # 원래 있던거 제거하고
                    answer.append([st+1, end]) # 추가
            else: # 비어있으면 그냥 추가
                answer.append([st+1, end])
        
        tmp_list[gems[st]] -= 1
        if tmp_list[gems[st]] == 0:
            tmp_sort.remove(gems[st])
            del tmp_list[gems[st]]
    return answer[0]