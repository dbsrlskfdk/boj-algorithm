import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(graph, v, color, visited):
    que = deque([v])
    while que:
        v = que.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]: # 방문하지 않은 vertex면, color의 초기화가 필요
                que.append(i)
                color[i] = color[v] % 2 + 1 # 이전 vertex의 color와 겹치지 않게 하기 위해서, %2 트릭 사용
            elif color[i] == color[v]: # 방문한 노드라면, color가 이전과 같은지 확인 필요
                return False # 이전과 같으면, 이분그래프가 아님으로, 바로 False 반환
    return True # 모든 순회가 정상적으로 끝났다면, 이분 그래프라는 의미. True 반환

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph =  defaultdict(list)
    color = [0] * (V+1)
    visited = [False] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)   
    
    for i in range(1, V+1):
        if not visited[i]:
            if color[i] == 0:
                color[i] = 1
            if not bfs(graph, i, color, visited):
                print("NO")
                break
    else:
        print("YES")