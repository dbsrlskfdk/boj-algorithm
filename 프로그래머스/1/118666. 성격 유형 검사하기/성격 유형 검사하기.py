from collections import defaultdict

def solution(survey, choices):
    answer = ''
    personal_type = ["RT", "CF", "JM", "AN"]
    total = defaultdict(int)
    for i, item in enumerate(choices):
        if item < 4:
            total[survey[i][0]] += 4 - item
        elif item > 4:
            total[survey[i][1]] += item - 4
    
    for per in personal_type:
        if total[per[0]] > total[per[1]]:
            answer += per[0]
        elif total[per[0]] < total[per[1]]:
            answer += per[1]
        else:
            answer += per[0]
    return answer