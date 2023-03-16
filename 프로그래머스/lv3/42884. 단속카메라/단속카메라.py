def solution(routes):
    answer = 0
    roads = sorted(routes, key=lambda x : x[0])
    roads = sorted(roads, key=lambda x : x[1])
    print(roads)
    past_end_point = -999999
    for road in roads:
        if past_end_point < road[0]:
            answer += 1
            past_end_point = road[1]

    return answer