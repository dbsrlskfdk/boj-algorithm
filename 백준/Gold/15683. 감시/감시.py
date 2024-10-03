N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
cam_positions = [(i, j) for i in range(N) for j in range(M) if (maps[i][j] and maps[i][j] != 6)]

# ↑, →, ↓, ← : 시계 방향으로 인덱스
directions = [
    [],
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],  # 1번 cctv
    [[1, 0, 1, 0], [0, 1, 0, 1]],  # 2번 cctv
    [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]],  # 3번 cctv
    [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]],  # 4번 cctv
    [[1, 1, 1, 1]],
]
watched = {}
watch_maps = set([(i, j) for i in range(N) for j in range(M) if maps[i][j] != 6])

for i, j in cam_positions:
    watched[(i, j)] = []
    for up_direction, right_direction, down_direction, left_direction in directions[maps[i][j]]:
        tmp_watched = set([(i, j)])    
        if up_direction:
            for y in range(i-1, -1, -1):
                if maps[y][j] != 6:
                    tmp_watched.add((y, j))
                else:
                    break
        if right_direction:
            for x in range(j+1, M):
                if maps[i][x] != 6:
                    tmp_watched.add((i, x))
                else:
                    break
        if down_direction:
            for y in range(i+1, N):
                if maps[y][j] != 6:
                    tmp_watched.add((y, j))
                else:
                    break
        if left_direction:
            for x in range(j-1, -1, -1):
                if maps[i][x] != 6:
                    tmp_watched.add((i, x))
                else:
                    break
        
        watched[(i, j)].append(tmp_watched)

watched_items = list(watched.values())
n_cams = len(cam_positions)

min_val = float('inf')
def dfs(n, total_watch):
    global min_val
    if n == n_cams:
        min_val = min(min_val, len(watch_maps - total_watch))
        return
    
    for i in range(len(watched_items[n])):
        dfs(n+1, total_watch.union(watched_items[n][i]))
        
dfs(0, set())
print(min_val)