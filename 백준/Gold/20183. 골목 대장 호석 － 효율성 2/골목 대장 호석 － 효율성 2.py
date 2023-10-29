from collections import defaultdict
import heapq

N, M, A, B, C = map(int, input().split())
graph = defaultdict(list)
costs = []

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((cost, y))
    graph[y].append((cost, x))
    heapq.heappush(costs, -cost)
    
L = 0
R = -heapq.heappop(costs)
ans = float('inf')

def dijkstra(mid):
    heap = []
    dist = [float('inf')] * (N + 1)
    heapq.heappush(heap, (0, A))
    dist[A] = 0
    
    while heap:
        c, v = heapq.heappop(heap)
        if dist[v] < c:
            continue
        for nc, nv in graph[v]:
            if nc > mid: # mid보다 큰 cost는 무시
                continue
            if dist[nv] > c + nc:
                dist[nv] = c + nc
                heapq.heappush(heap, (c + nc, nv))
                
                if nv == B and dist[nv] <= C: # B에 도착했을 때 C보다 작은 cost면 True
                    return True
    return False

while L <= R:
    mid = (L + R) // 2
    if dijkstra(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1

if ans == float('inf'):
    print(-1)
else:
    print(ans)