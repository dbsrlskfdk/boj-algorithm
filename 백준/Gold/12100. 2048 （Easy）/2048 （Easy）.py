N = int(input())
nums = [[int(i) for i in input().split()] for _ in range(N)]

def move_up(nums, prev_max):
    """
    위로 이동하는 함수
    1. 빈칸(0)이 아닌 숫자블럭들을 row별로 모두 체크
    2. 앞에서부터 합쳐서 다시 넣어주기
    """
    tmp_max = prev_max
    
    tmp_arr = [[-1] for _ in range(N)] # column별로 row의 빈칸(0)이 아닌 숫자들을 모아놓은 arr : [i, j] => 실제 nums의 i-th column의 0이 아닌 숫자들임
    for j in range(N):
        for i in range(N):
            if nums[i][j]: # 빈칸이 아니라면
                if tmp_arr[j][-1] == nums[i][j]: # 가장 마지막에 값과, 현재 체크할 값이 같으면 합쳐져야함
                    tmp_arr[j][-1] *= 2 # 2배, 어차피 2의 제곱수라
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
                    if i != N-1:
                        tmp_arr[j].append(-1) # 합쳐졌으면, 뒤에 오는 값들과 다시 합쳐지지않게 -1로 경계값을 체크하도록
                elif tmp_arr[j][-1] == -1: # 만약 마지막 값이 -1로 같지 않았으면,
                    tmp_arr[j].pop() # 경계 체크용 값이기에 뽑고 넣어줌
                    tmp_arr[j].append(nums[i][j]) # 만약 같지않으면, 그냥 넣어준다
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
                else:
                    tmp_arr[j].append(nums[i][j]) # 그 외 다른 값으로 같지않았다면, 그냥 넣어준다.
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
            elif i == N-1 and tmp_arr[j][-1] == -1:
                tmp_arr[j].pop()

    res = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(tmp_arr):
        for j, v in enumerate(row):
            res[j][i] = v

    return res, tmp_max


            

def move_down(nums, prev_max):
    """
    아래로 이동하는 함수

    """
    tmp_max = prev_max
    tmp_arr = [[-1] for _ in range(N)] # column별로 row의 빈칸(0)이 아닌 숫자들을 모아놓은 arr : [i, j] => 실제 nums의 i-th column의 0이 아닌 숫자들임
    for j in range(N):
        for i in range(N-1, -1, -1):
            if nums[i][j]: # 빈칸이 아니라면
                if tmp_arr[j][-1] == nums[i][j]: # 가장 마지막에 값과, 현재 체크할 값이 같으면 합쳐져야함
                    tmp_arr[j][-1] *= 2 # 2배, 어차피 2의 제곱수라
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
                    if i != 0:
                        tmp_arr[j].append(-1) # 합쳐졌으면, 뒤에 오는 값들과 다시 합쳐지지않게 -1로 경계값을 체크하도록
                elif tmp_arr[j][-1] == -1: # 만약 마지막 값이 -1로 같지 않았으면,
                    tmp_arr[j].pop() # 경계 체크용 값이기에 뽑고 넣어줌
                    tmp_arr[j].append(nums[i][j]) # 만약 같지않으면, 그냥 넣어준다
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
                else:
                    tmp_arr[j].append(nums[i][j]) # 그 외 다른 값으로 같지않았다면, 그냥 넣어준다.
                    tmp_max = max(tmp_max, tmp_arr[j][-1]) # max값 체크
            elif i == 0 and tmp_arr[j][-1] == -1:
                tmp_arr[j].pop()

    res = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(tmp_arr):
        for j, v in enumerate(row):
            res[(N-1)-j][i] = v

    return res, tmp_max

def move_left(nums, prev_max):
    tmp_max = prev_max
    # 왼쪽으로 이동하는 함수
    tmp_arr = [[-1] for _ in range(N)] # column별로 row의 빈칸(0)이 아닌 숫자들을 모아놓은 arr : [i, j] => 실제 nums의 i-th column의 0이 아닌 숫자들임
    for i in range(N):
        for j in range(N):
            if nums[i][j]: # 빈칸이 아니라면
                if tmp_arr[i][-1] == nums[i][j]: # 가장 마지막에 값과, 현재 체크할 값이 같으면 합쳐져야함
                    tmp_arr[i][-1] *= 2 # 2배, 어차피 2의 제곱수라
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
                    if j != N-1:
                        tmp_arr[i].append(-1) # 합쳐졌으면, 뒤에 오는 값들과 다시 합쳐지지않게 -1로 경계값을 체크하도록
                elif tmp_arr[i][-1] == -1: # 만약 마지막 값이 -1로 같지 않았으면,
                    tmp_arr[i].pop() # 경계 체크용 값이기에 뽑고 넣어줌
                    tmp_arr[i].append(nums[i][j]) # 만약 같지않으면, 그냥 넣어준다
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
                else:
                    tmp_arr[i].append(nums[i][j]) # 그 외 다른 값으로 같지않았다면, 그냥 넣어준다.
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
            elif j == N-1 and tmp_arr[i][-1] == -1:
                tmp_arr[i].pop()

    res = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(tmp_arr):
        for j, v in enumerate(row):
            res[i][j] = v

    return res, tmp_max
def move_right(nums, prev_max):
    tmp_max = prev_max
    tmp_arr = [[-1] for _ in range(N)] # column별로 row의 빈칸(0)이 아닌 숫자들을 모아놓은 arr : [i, j] => 실제 nums의 i-th column의 0이 아닌 숫자들임
    for i in range(N):
        for j in range(N-1, -1, -1):
            if nums[i][j]: # 빈칸이 아니라면
                if tmp_arr[i][-1] == nums[i][j]: # 가장 마지막에 값과, 현재 체크할 값이 같으면 합쳐져야함
                    tmp_arr[i][-1] *= 2 # 2배, 어차피 2의 제곱수라
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
                    if j != 0:
                        tmp_arr[i].append(-1) # 합쳐졌으면, 뒤에 오는 값들과 다시 합쳐지지않게 -1로 경계값을 체크하도록
                elif tmp_arr[i][-1] == -1: # 만약 마지막 값이 -1로 같지 않았으면,
                    tmp_arr[i].pop() # 경계 체크용 값이기에 뽑고 넣어줌
                    tmp_arr[i].append(nums[i][j]) # 만약 같지않으면, 그냥 넣어준다
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
                else:
                    tmp_arr[i].append(nums[i][j]) # 그 외 다른 값으로 같지않았다면, 그냥 넣어준다.
                    tmp_max = max(tmp_max, tmp_arr[i][-1]) # max값 체크
            elif j == 0 and tmp_arr[i][-1] == -1:
                tmp_arr[i].pop()

    res = [[0 for _ in range(N)] for _ in range(N)]
    for i, row in enumerate(tmp_arr):
        for j, v in enumerate(row):
            res[i][N-1-j] = v

    return res, tmp_max


max_val = 0
def find_max(nums, prev_max, depth):
    global max_val
    # print(f"Depth : {depth}")
    up_res, up_max = move_up(nums, prev_max)
    down_res, down_max = move_down(nums, prev_max)
    left_res, left_max = move_left(nums, prev_max)
    right_res, right_max = move_right(nums, prev_max)

    max_res = max(up_max, down_max, left_max, right_max)

    if depth == 5:
        max_val = max(max_res, max_val)
        return
    else:
        find_max(up_res, max_res, depth+1)
        find_max(down_res, max_res, depth+1)
        find_max(left_res, max_res, depth+1)
        find_max(right_res, max_res, depth+1)

find_max(nums, 0, 1)
print(max_val)