import heapq
from collections import defaultdict

def solution(alp, cop, problems):
    answer = 0
    max_alp = max([i[0] for i in problems]) # 문제에 alp_req 중 가장 큰 값
    max_cop = max([i[1] for i in problems]) # 문제에 cop_req 중 가장 큰 값
    alp = min(alp, max_alp) # 초깃 값 alp가, max_alp보다 클 경우 max_alp로 변경
    cop = min(cop, max_cop) # 초깃 값 cop가, max_cop보다 클 경우 max_cop로 변경
    dp = [[float('inf') for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    graphs = defaultdict(list)
    
    for i in range(len(problems)):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
        graphs[(alp_req, cop_req)].append((alp_rwd, cop_rwd, cost))
    
    heap = []
    heapq.heappush(heap, (0, alp, cop))
    
    while heap:
        c, calp, ccop = heapq.heappop(heap)
        if dp[calp][ccop] < c:
            continue
        if calp + 1 <= max_alp:
            if dp[calp+1][ccop] > dp[calp][ccop] + 1:
                dp[calp+1][ccop] = dp[calp][ccop] + 1
                heapq.heappush(heap, (dp[calp+1][ccop], calp+1, ccop))
        if ccop + 1 <= max_cop:
            if dp[calp][ccop+1] > dp[calp][ccop] + 1:
                dp[calp][ccop+1] = dp[calp][ccop] + 1
                heapq.heappush(heap, (dp[calp][ccop+1], calp, ccop+1))
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if calp >= alp_req and ccop >= cop_req:
                if dp[min(calp + alp_rwd, max_alp)][min(ccop + cop_rwd, max_cop)] > dp[calp][ccop] + cost:
                    dp[min(calp + alp_rwd, max_alp)][min(ccop + cop_rwd, max_cop)] = dp[calp][ccop] + cost
                    heapq.heappush(heap, (dp[min(calp + alp_rwd, max_alp)][min(ccop + cop_rwd, max_cop)], min(calp + alp_rwd, max_alp), min(ccop + cop_rwd, max_cop)))
    
    answer = dp[-1][-1]
    return answer