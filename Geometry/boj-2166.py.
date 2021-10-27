N = int(input())
coordinates = [list(map(int, input().split(" "))) for _ in range(N)]

sum = 0
for i in range(N-1):
    sum += coordinates[i][0] * coordinates[i+1][1]
    sum -= coordinates[i+1][0] * coordinates[i][1]
sum += coordinates[N-1][0] * coordinates[0][1]
sum -= coordinates[0][0] * coordinates[N-1][1]

sum = abs(sum) / 2

print(sum)
