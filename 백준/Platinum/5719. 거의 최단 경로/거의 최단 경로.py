from collections import defaultdict, deque
import heapq, sys

input = sys.stdin.readline

def dijkstra(S, N, graphs):
    heap = []
    dist = [float('inf')] * N
    dist[S] = 0
    heapq.heappush(heap, (0, S))
    
    while heap:
        c, v = heapq.heappop(heap)
        if dist[v] < c:
            continue
            
        for nv, nc in graphs[v].items():
            if dist[nv] > c + nc:
                dist[nv] = c + nc
                heapq.heappush(heap, (dist[nv], nv))
    
    return dist
    
def delete_edge(S, D, min_dist, dist_dict):
    del_list = []
    que = deque([D])
    
    while que:
        v = que.popleft()
        if v == S:
            continue
        for nc, nv in graphs[v]:
            if min_dist[nv] + nc == min_dist[v] and (nv, v) not in del_list:
                del_list.append((nv, v))
                que.append(nv)
                
    for v, nv in del_list:
        del dist_dict[v][nv]
    
N, M = map(int, input().split())
while not(N == 0 and M == 0):
    S, D = map(int, input().split())
    graphs = defaultdict(list)
    dist_dict = defaultdict(dict)
    for _ in range(M):
        U, V, P = map(int, input().split())
        dist_dict[U][V] = P
        graphs[V].append((P, U))   
    
    min_dist = dijkstra(S, N, dist_dict)
    
    delete_edge(S, D, min_dist, dist_dict)
    
    min_dist = dijkstra(S, N, dist_dict)
    print(min_dist[D] if min_dist[D] != float('inf') else -1)
    N, M = map(int, input().split())