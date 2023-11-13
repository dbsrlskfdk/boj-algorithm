import heapq
from collections import defaultdict

def dijkstra(graphs, summits, gates, n):
    heap = []
    dist = [float('inf')] * (n+1)
    visited = [False] * (n+1)

    for gate in gates:
        dist[gate] = 0
        heapq.heappush(heap, (0, gate))
    
    while heap:
        c, v = heapq.heappop(heap)
        if (dist[v] < c and visited[v]) or v in summits:
            continue
        
        visited[v] = True
        for nv, nw in graphs[v]:
            if nv in gates:
                continue
            if dist[nv] > max(c, nw):
                dist[nv] = max(c, nw)
                if not visited[nv]:
                    heapq.heappush(heap, (dist[nv], nv))
    return dist


def solution(n, paths, gates, summits):
    answer = []
    summits.sort()
    hashed_gates = set(gates)
    hashed_summits = set(summits)
    graphs = defaultdict(list)
    for u, v, w in paths:
        graphs[u].append((v, w))
        graphs[v].append((u, w))
        
    dist = dijkstra(graphs, hashed_summits, hashed_gates, n)
    
    answer = [0, float('inf')]
    for summit in summits:
        if dist[summit] < answer[1]:
            answer = [summit, dist[summit]]
    return answer