import heapq

def solution(stones, k):
    answer = 0
    heap = [(-1*v, i) for i, v in enumerate(stones[:k])]
    heapq.heapify(heap)
    answer = -1 * heap[0][0]
    for i in range(k, len(stones)):
        heapq.heappush(heap, (-1*stones[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        answer = min(answer, -1*heap[0][0])
    return answer