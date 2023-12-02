import heapq, sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    min_heap = []
    max_heap = []
    deleted = [0] * N
    for i in range(N):
        cmd = input().split()
        
        if cmd[0] == "I":
            heapq.heappush(min_heap, (int(cmd[1]), i))
            heapq.heappush(max_heap, (-int(cmd[1]), i))
        elif cmd[0] == "D":
            if cmd[1] == "-1":
                if min_heap:
                    deleted[heapq.heappop(min_heap)[1]] = 1
                
            elif cmd[1] == "1":
                if max_heap:
                    deleted[heapq.heappop(max_heap)[1]] = 1
        while min_heap and deleted[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and deleted[max_heap[0][1]]:
            heapq.heappop(max_heap)
            
    if not min_heap and not max_heap:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])