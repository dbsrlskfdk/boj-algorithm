from collections import deque

def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    que1_sum = sum(queue1)
    que2_sum = sum(queue2)
    half = (que1_sum + que2_sum) / 2
    
    while not ((que1_sum == half) and (que2_sum == half)):
        if que1_sum > half:
            que1_pop = que1.popleft()
            que2.append(que1_pop)
            que1_sum -= que1_pop
            que2_sum += que1_pop
            answer += 1
        elif que2_sum > half:
            que2_pop = que2.popleft()
            que1.append(que2_pop)
            que1_sum += que2_pop
            que2_sum -= que2_pop
            answer += 1
        
        if (que1_sum >= half and len(que1)==1) and (que2_sum < half):
            answer = -1
            break
        elif (que2_sum >= half and len(que2)==1) and (que1_sum < half):
            answer = -1
            break
        
        if answer >= 600_000:
            answer = -1
            break
    return answer