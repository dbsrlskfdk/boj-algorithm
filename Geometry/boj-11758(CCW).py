N = 3
coordinates = [list(map(int, input().split(" "))) for _ in range(N)]

sum = 0
for i in range(N-1):
    sum += coordinates[i][0] * coordinates[i+1][1]
    sum -= coordinates[i+1][0] * coordinates[i][1]
sum += coordinates[N-1][0] * coordinates[0][1]
sum -= coordinates[0][0] * coordinates[N-1][1]

# 외적값의 부호에 따른 방향성을 판단할 수 있다는데, 수학적인 내용이라 공부가 필요
if sum > 0:
    print(1)
elif sum < 0:
    print(-1)
else:
    print(0)
