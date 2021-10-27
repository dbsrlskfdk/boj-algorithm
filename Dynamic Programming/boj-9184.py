num_list = [[[0 for z in range(21)] for y in range(21)] for x in range(21)]  # 어차피  20 넘어가는 숫자들은 20의 값을 쓰니까 이 이상 필요없음

def w(a, b, c, p_list):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, p_list)

    if p_list[a][b][c] != 0: # 0이 아니면 굳이 조건을 시행하여 계산할 필요가 없기에, 리스트에 있는 수를 반환 #// 이거 안해줘서 자꾸 recursion 들어감.. ㅠ 조심하자
        return p_list[a][b][c]

    if a < b and b < c:
        p_list[a][b][c] = w(a, b, c-1, p_list) + w(a, b-1, c-1, p_list) - w(a, b-1, c, p_list)
        return p_list[a][b][c]

    p_list[a][b][c] = w(a-1, b, c, p_list) + w(a-1, b-1, c, p_list) + w(a-1, b, c-1, p_list) - w(a-1, b-1, c-1, p_list)
    return p_list[a][b][c]

a, b, c = map(int, input().split(" "))

while not (a == -1 and b == -1 and c == -1):
    print(f'w({a}, {b}, {c}) = {w(a, b, c, num_list)}')
    a, b, c = map(int, input().split(" "))
