N = int(input())
num_list = []
for i in range(N):
    age, name = list(input().split(" "))
    num_list.append([int(age), name])
sort_list = sorted(num_list, key= lambda x: x[0])
for i in range(len(sort_list)):
    print(sort_list[i][0], sort_list[i][1])
