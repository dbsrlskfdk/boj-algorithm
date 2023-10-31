from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
	a, b = map(int, input().split())
	graph[a].append((i, b))
	graph[b].append((i, a))
    
heap = []
cost = [float('inf')] * (N + 1)
visited = [False] * (N + 1)

cost[1] = 0
heapq.heappush(heap, (0, 1, 0))

while heap:
	cum_c, v, c  = heapq.heappop(heap)
	if cost[v] < cum_c and visited[v]:
		continue
	visited[v] = True
	for nc, nv in graph[v]:
		if cum_c % M <= nc:
			time = nc - (cum_c % M) + 1
		elif cum_c % M > nc:
			time = nc - (cum_c % M) + M + 1
		
		if cost[nv] > time + cum_c:
			cost[nv] = time + cum_c
			if not visited[nv]:
				heapq.heappush(heap, (cost[nv], nv, nc))
                
print(cost[N])