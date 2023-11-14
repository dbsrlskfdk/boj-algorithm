from collections import deque


def check_distance(place):
    participants = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                participants.append([i,j])
            
    for i in range(len(participants)):    
        y1, x1 = participants[i]
        visited = [[False]*5 for _ in range(5)]
        distance = [[float('inf')]*5 for _ in range(5)]
        que = deque([[y1, x1]])
        visited[y1][x1] = True
        distance[y1][x1] = 0
        
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]
        while que:
            y, x = que.popleft()
            for q in range(4):
                ny = y + dy[q]
                nx = x + dx[q]
                if 0<=ny<5 and 0<=nx<5 and not visited[ny][nx] and place[ny][nx] != 'X':
                    visited[ny][nx] = True
                    distance[ny][nx] = min(distance[ny][nx], distance[y][x] + 1)
                    que.append([ny,nx])
        
        for j in range(len(participants)):
            if i != j:
                y2, x2 = participants[j]
                if abs(distance[y1][x1] - distance[y2][x2]) <= 2:
                    print(f"partipant {y1, x1} - {y2, x2} Infection")
                    return 0
        
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))

    return answer