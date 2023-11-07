from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N, M = map(int, input().split())
graphs = defaultdict(list)
for _ in range(M):
    a, b, cost = map(int, input().split())
    graphs[a].append((b, cost))
    graphs[b].append((a, cost))
    
for i in range(1, N+1):
    graphs[i].sort() # 사전순으로 탐색을 하기위해서, 그래프의 모든 노드들 정렬

S, E = map(int, input().split())

def dijkstra(visited, st):
    dist = [float('inf')] * (N+1)
    dist[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))
    while heap:
        c, v = heapq.heappop(heap)
        if dist[v] < c and visited[v]:
            continue
        visited[v] = True
        for nv, nc in graphs[v]:
            if dist[nv] > c + nc:
                dist[nv] = c + nc
                if not visited[nv]:
                    heapq.heappush(heap, (dist[nv], nv))
    return dist

dist = dijkstra([False] * (N+1), E)
cost = 0
cur = S
visited = [False] * (N+1)

while cur != E:
    for nv, nc in graphs[cur]: # 현재 노드에서 갈 수 있는 모든 노드를 탐색한다.
        if cost + nc + dist[nv] == dist[S]: # 최단 경로에 포함되는 엣지면,
            cost += nc # 해당 엣지의 비용을 더한다.
            visited[cur] = True # 그리고 방문 처리하여, 돌아오는길에서 다시 탐색하지 않도록 한다.
            cur = nv # 커서를 다음 노드로 이동하여, 다시 탐색하도록 한다.
            break
            
dist = dijkstra(visited, S) # 사전순으로 구한 최단거리의 경로에 포함되는 노드를 방문하지않도록, 시작점부터 각 노드까지의 최단거리를 구한다.
print(cost + dist[E])