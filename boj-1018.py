N, M = map(int, input().split(" "))
board_list = []

for i in range(N):
    board_list.append(input())
result = 64 # 전체 다 바꾸는 뒤집어주는 케이스는 64보다는 작을 것이므로, result를 64로 고정하고 시작.
segment_list=[]
for start_i in range(N-7):
    for start_j in range(M-7):
        first_cnt_B = 0
        first_cnt_W = 0
        for i in range(start_i, start_i + 8):
            for j in range(start_j, start_j + 8):
                if (i+j) % 2 == 0:
                    if board_list[i][j] != 'B': # (i+j) 가 짝수이면, 그니까 (0,0), (0,2), (0,4) (1,3) 같은 곳, 시작이 B인 case에 대해서 Black이 아니면, 블랙 횟수 하나 업
                        first_cnt_B += 1
                    if board_list[i][j] != 'W': # (i+j) 가 짝수이면, 그니까 (0,0), (0,2), (0,4) (1,3) 같은 곳, 시작이 W인 case에 대해서 White이 아니면, 화이트 횟수 하나 업
                        first_cnt_W += 1 
                else:
                    if board_list[i][j] != 'B': # (i+j) 가 홀수이면, (0,1) , (0, 3) 시작이 W, 홀수인 부분은 다 'B'가 돼야한다. 그렇기에 'B'가 아니면 W로 바꿔줘야하므로, 화이트 횟수 하나 업
                        first_cnt_W += 1
                    if board_list[i][j] != 'W': # (i+j) 가 홀수이면, (0,1) , (0, 3) 시작이 B, 홀수인 부분은 다 'W'가 돼야한다. 그렇기에 'W'가 아니면 B로 바꾸어줘야하므로, 블랙 횟수 하나 업
                        first_cnt_B += 1
        result =  min(result, first_cnt_B, first_cnt_W) # 패턴을 옮겨가면서, 원래 저장되어있던 result랑 이 패턴에서 새로 나온 횟수에 대해서 최솟값을 result에 저장

print(result)
