from collections import deque
N = int(input())
K = int(input())
apples = [list(map(int, input().split(" "))) for _ in range(K)]
L = int(input())
turning = [(lambda x : [int(x[0]),x[1]])(input().split(" ")) for _ in range(L)]
board = []
for i in range(N+2):
    tmp_row = []
    for j in range(N+2):
        if j == N+1:
            tmp_row.append("#")
            board.append(tmp_row)
        elif i == 0 or i == N+1 or j == 0:
            tmp_row.append("#")
        else:
            if [i, j] in apples:
                tmp_row.append("A")
            else:
                tmp_row.append(" ")

snake = deque([[1, 1]])
board[snake[0][0]][snake[0][1]] = '■'

time = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir_idx = 0
while (1 <= snake[0][0] <= N) and (1 <= snake[0][1] <= N):
    time += 1
    dy = snake[0][0] + direction[dir_idx][0]
    dx = snake[0][1] + direction[dir_idx][1]
    snake.appendleft([dy, dx])
    if (1 <= dy <= N) and (1 <= dx <= N):
        if board[dy][dx] == 'A': # 칸이 사과이면
            board[dy][dx] = '■' # 그냥 '■' 만 해준다.
        elif board[dy][dx] == ' ': # 칸에 사과가 없으면
            board[snake[-1][0]][snake[-1][1]] = ' ' # 꼬리 부분을 초기화
            board[dy][dx] = '■'
            snake.pop()
        elif board[dy][dx] == '■':
            break
    else:
        break

    if len(turning) != 0 and time == turning[0][0]:
        if turning[0][1] == "D":
            dir_idx += 1
            dir_idx = dir_idx % 4
        else:
            dir_idx -= 1
            if dir_idx < 0:
                dir_idx = 3
        turning.pop(0)
    

print(time)