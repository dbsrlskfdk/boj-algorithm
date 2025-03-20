import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M = int(input())

    L = [] # mid보다 작은값을 저장할 최대힙
    R = [] # mid보다 큰값을 저장할 최소힙
    
    answer = []
    arrs = []
    # 입력단, 10개 제한으로 줄나눔 받음
    for i in range(M//10+1):
        arrs.extend(list(map(int, input().split())))

    mid = arrs[0]
    answer.append(mid)
    # 처리 로직
    for i, d in enumerate(arrs):
        if i != 0:
            if d > mid: # mid 보다 크면, R(ight)에 저장
                heapq.heappush(R, d)
            else: # mid 보다 작으면,  L(ight)에 저장
                heapq.heappush(L, -d)
            
        if i != 0 and (i+1) % 2 : # 홀수번째 숫자에 도달하면,
            if len(L) > len(R): # mid 기준 L(eft)의 갯수가 R(ight)의 갯수보다 많으면, 중앙값이 아님
                heapq.heappush(R, mid) # R(ight)에 기존의 중앙값을 넣고,
                mid = -heapq.heappop(L) #L(eft)에서 최댓값을 빼서 mid 갱신
            elif len(L) < len(R):
                heapq.heappush(L, -mid) # L(eft)에 기존의 중앙값을 넣고
                mid = heapq.heappop(R) # R(right)에서 최솟값을 빼서 mid갱신
            
            answer.append(mid)

    # 출력단, 10개 제한으로 줄나눔 출력
    len_mid = len(answer)
    print(len_mid)
    for i in range(len_mid // 10 + 1):
        print(*answer[i*10:(i+1)*10])