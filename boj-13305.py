N = int(input())
distance = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))

min_cost = cost[0]
sum = cost[0] * distance[0]

for i in range(1, N-1):
    min_cost = min(min_cost, cost[i])
    sum += min_cost * distance[i]
print(sum)
