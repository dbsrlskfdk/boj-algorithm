"""
사다리 타기 문제.
모든 사다리의 세로선이 동일한 세로선에서 끝나는 데 필요한 '최소'의 가로선의 갯수를 구하는 프로그램

하지만, 정답의 갯수가 3보다 크거나, 불가능하면 -1을 return
"""
import sys

input = sys.stdin.readline

def check() -> bool:
    """
    세로선 i의 끝이 i가 나오는지 판단하는 함수

    :return bool:
    """
    for st in range(N): # 모든 세로선에 대해서 체크
        cur = st
        for h in range(H):
            if ladders[h][cur]: # 가로선이 오른쪽 진행 방향에 존재
                cur += 1
            elif cur > 0 and ladders[h][cur-1]: # 가로선이 왼쪽 진행 방향에 존재
                cur -= 1

        if cur != st:
            return False
    return True

def dfs(n: int, coords):
    global cnt
    # 3보다 크면, 최댓값 넘어가기에 종료
    if n > 3 or cnt <= n:
        return

    # 세로선 조건 체크
    if check():
        cnt = min(cnt, n)
        return

    # 탐색을 시작할 좌표
    y, x = coords

    # 탐색 시작
    for i in range(y, H):
        if i == y: # 행이 변경되기 전에는 현재 세로선 위치부터 탐색
            st_x = x
        else: # 행이 변경되고 나서는 처음 세로선 위치부터 탐색
            st_x = 0

        for j in range(st_x, N-1):
            if not ladders[i][j] and not ladders[i][j+1]: # 탐색 위치, 탐색 위치 이후에 가로선이 없다면
                ladders[i][j] = True # 현재 위치에 가로선 놓기
                dfs(n+1, [i, j+2]) # 가로선 갯수 1개 늘리기, 탐색 좌표 열을 +2 위치부터 시작(가로선을 연속해서 놓을 순 없기때문에)
                ladders[i][j] = False # 현재 위치 가로선 제거


cnt = float('inf')
# N : 세로선의 갯수, M : 가로선의 갯수, H : 세로선마다 가로선을 놓을 수 있는 위치의 갯수
N, M, H = map(int, input().split())

# 사다리의 세로선과 가로선의 교차점을 표현
# 만약 (n ,h) = (1,1)이면 세로선 1 -> 세로선 2로 가는 가로선이 가로선 가능 위치 1에 위치에 있다는 것
ladders = [[False] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladders[a-1][b-1] = True

dfs(0, [0, 0])
print(cnt if cnt < 4 else -1)
