def make_dragon_curv(curv):
    """
    시작 점(x, y), 방향(d), 세대(g)를 통해 드래곤 커브를 만드는 함수
    드래곤 커브는 세대가 늘어날 때마다, 가장 끝 점을 기준으로 (시계 방향으로 90도 회전) 시킨 다음
    이전 세대에 이어 붙인다.

    특정 점 (a, b)를 기준으로 (x, y)를 이동하는 방법
    1. 기준점을 원점으로 이동하기 위해 (x, y)에서 기준점의 좌표를 뺀다
    (x, y) -> (x-a, y-b)

    2. 이동된 좌표를 원점 기준으로 회전한다.
    - 반시계 방향 90도 회전 : (x, y) -> (-y, x)
    - 시계 방향 90도 회전 : (x, y) -> (y, -x)
    여기선 시계 방향 90도 회전임으로 좌표는
    (x-a, y-b) -> (y-b, -(x-a))

    3. 회전된 좌표를 다시 기준점으로 이동한다.
    (y-b + a, -x+a + b)

    :return:
    """
    x, y, d, g = curv
    mat[y][x] = True
    curv_coords = [[x, y]]
    # 0세대 드래곤 커브
    if d == 0:
        nx, ny = x+1, y
    elif d == 1:
        nx, ny = x, y-1
    elif d == 2:
        nx, ny = x-1, y
    else:
        nx, ny = x, y+1

    mat[ny][nx] = True
    curv_coords.append([nx, ny])

    # 1세대 드래곤 커브 ~
    for gen in range(1, g+1):
        a, b = curv_coords[-1]
        for x, y in curv_coords[-2::-1]:
            nx, ny = -y + b + a, x - a + b
            mat[ny][nx] = True
            curv_coords.append([nx, ny])

def count_square() -> int:
    """
    네 꼭짓점이 모두 드래곤 커브의 일부인 1x1정사각형의 갯수를 찾는 함수
    :return:
    """
    cnt = 0
    for i in range(100):
        for j in range(100):
            if mat[i][j] and mat[i][j+1] and mat[i+1][j] and mat[i+1][j+1]:
                cnt += 1
    return cnt
"""
드래곤 커브의 입력은 [x, y, d, g]로 주어진다.
각 값의 의미는
- x, y : 드래곤 커브의 시작 점
- d : 시작 방향 (0 : x증가 방향(->), 1 : y 감소 방향, 2 : x감소 방향(<-), 3 : y 증가 방향)
- g : 드래곤 커브 세대 
"""
N = int(input())
curvs = [list(map(int, input().split())) for _ in range(N)]
mat = [[False] * 101 for _ in range(101)]

for curv in curvs:
    make_dragon_curv(curv)

ans = count_square()
print(ans)