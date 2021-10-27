L1 = list(map(int, input().split(" "))) # (x1, y1), (x2, y2)
L2 = list(map(int, input().split(" "))) # (x3, y3), (x4, y4)

ccw_list_1 = [L1[0:2], L1[2:4], L2[0:2]]
ccw_list_2 = [L1[0:2], L1[2:4], L2[2:4]]
ccw_list_3 = [L2[0:2], L2[2:4], L1[0:2]]
ccw_list_4 = [L2[0:2], L2[2:4], L1[2:4]]
def CCW(coordinates):
    N=3
    sum = 0
    for i in range(N-1):
        sum += coordinates[i][0] * coordinates[i+1][1]
        sum -= coordinates[i+1][0] * coordinates[i][1]
    sum += coordinates[N-1][0] * coordinates[0][1]
    sum -= coordinates[0][0] * coordinates[N-1][1]
    return sum

if CCW(ccw_list_1) * CCW(ccw_list_2) < 0 and CCW(ccw_list_3) * CCW(ccw_list_4) < 0:
    print(1)
else:
    print(0)
