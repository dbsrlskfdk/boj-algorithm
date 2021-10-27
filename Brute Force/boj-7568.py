N = int(input())
weight_height = []
rank = [1] * N
for i in range(N):
    weight_height.append(list(map(int, input().split(" "))))

for i in range(N):
    for j in range(N):
        if weight_height[i][0] < weight_height[j][0] and weight_height[i][1] < weight_height[j][1]:
            rank[i] += 1

for i in range(N):
    print(rank[i], end= ' ')
