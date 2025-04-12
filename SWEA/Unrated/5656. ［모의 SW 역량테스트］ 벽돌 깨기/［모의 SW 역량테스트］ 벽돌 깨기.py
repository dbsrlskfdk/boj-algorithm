"""
[지시]
- 구슬은 좌,우 로만 움직일 수 있음. 항상 맨 위의 벽돌만 깨뜨릴 수 있다.
- 벽돌은 숫자 1~9로 표현되며, 구슬이 명중한 벽돌은 상하좌우 (숫자-1)칸만큼 같이 제거됨
- 제거되는 범위 내에 있는 벽돌은 동시에 제거됨
- 빈 공간이 있을 경우 벽돌은 중력에 의해 밑으로 떨어진다.

N개의 구슬을 떨어트려, 최대한 많은 벽돌을 제거하려고 할 때,
남은 벽돌의 갯수를 구하기.

"""
import copy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return 0 <= y < H and 0 <= x < W

def down_blocks(prev_maps):
    new_maps = [[0] * W for _ in range(H)]
    for j in range(W):
        temp_col = []
        for i in range(H-1, -1, -1):
            if prev_maps[i][j] != 0:
                temp_col.append(prev_maps[i][j])

        for i, v in enumerate(temp_col):
            new_maps[H-1-i][j] = v

    return new_maps



def explosion(pos, prev_explosion, explosed_map, prev_maps):
    distance = prev_maps[pos[0]][pos[1]]

    cur_explosion = []
    for i in range(4):
        for d in range(distance):
            ny = pos[0] + dy[i]*d
            nx = pos[1] + dx[i]*d

            if in_range(ny, nx) and not explosed_map[ny][nx] and prev_maps[ny][nx]:
                cur_explosion.append((ny, nx))
                explosed_map[ny][nx] = True
                concurrent_explosion = explosion((ny, nx), prev_explosion+[(ny, nx)], explosed_map, prev_maps)
                if concurrent_explosion:
                    cur_explosion.extend(concurrent_explosion)
    return cur_explosion



def shoot_ball(c, prev_maps):
    """
    c열의 구슬을 떨어트리는 함수
    :param c: 구슬을 떨어트릴 열
    :return:
    """
    attach_block = None

    for i in range(H):
        if prev_maps[i][c] != 0:
            attach_block = [i, c]
            break

    if attach_block is None:
        return prev_maps

    new_maps = copy.deepcopy(prev_maps)
    explosed_block = explosion(attach_block, [], [[False]* W for _ in range(H)], new_maps)

    for i, j in explosed_block: # 터진 블록들은 0으로 없애주기
        new_maps[i][j] = 0

    return down_blocks(new_maps)


def recv_shoot(c, n, prev_maps):
    global min_block
    if n == N: # 모든 구슬을 다 쏘면,
        # 남은 구슬 세기
        cnt = 0
        for i in range(H):
            for j in range(W):
                if prev_maps[i][j]:
                    cnt += 1

        if cnt < min_block:
            min_block = cnt

        return prev_maps

    prev_maps = copy.deepcopy(prev_maps)
    for j in range(W):
        explosed_map = shoot_ball(j, prev_maps) # recv 0 -> explosion -> recv 00 -> explosion -> recv 000 -> end, exit -> recv 001 -> 이전 로컬변수들이 남아있음..
        recv_shoot(c+[j], n+1, explosed_map) # TODO: 참조 오류 해결하기..

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split()) # N: 쏠 구슬의 갯수, (H, W) : 벽돌 정보

    maps = [list(map(int, input().split())) for _ in range(H)]
    min_block = float('inf')
    for i in range(W):
        recv_shoot([], 0, maps)
    print(f"#{t} {min_block}")
