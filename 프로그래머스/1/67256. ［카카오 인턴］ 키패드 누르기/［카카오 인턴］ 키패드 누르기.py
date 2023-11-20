def solution(numbers, hand):
    answer = ''
    click = {
        "*": ("L", (0, 0)),
        0: ("M", (0, 1)),
        "#": ("R", (0, 2)),
        1: ("L", (3, 0)),
        2: ("M", (3, 1)),
        3: ("R", (3, 2)),
        4: ("L", (2, 0)),
        5: ("M", (2, 1)),
        6: ("R", (2, 2)),
        7: ("L", (1, 0)),
        8: ("M", (1, 1)),
9: ("R", (1, 2))}
    cur_l = "*"
    cur_r = "#"
    
    for num in numbers:
        if click[num][0] != "M":
            answer += str(click[num][0])
            if click[num][0] == "L":
                cur_l = num
            else:
                cur_r = num
        else:
            y, x = click[num][1]
            ly, lx = click[cur_l][1]
            ry, rx = click[cur_r][1]
            
            if abs(y-ly) + abs(x-lx) > abs(y-ry) + abs(x-rx): # 왼손의 거리가 더 크면
                answer += "R"
                cur_r = num
            elif abs(y-ly) + abs(x-lx) < abs(y-ry) + abs(x-rx):
                answer += "L"
                cur_l = num
            else:
                if hand == "left":
                    answer += "L"
                    cur_l = num
                elif hand == "right":
                    answer += "R"
                    cur_r = num
    
    return answer
            