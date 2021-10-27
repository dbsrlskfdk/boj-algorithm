import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split(" ")))
set_num = list(sorted(set(num_list)))
num_dic = {}

for i in range(len(set_num)):
    num_dic[set_num[i]] = i
    
for i in range(N):
    sys.stdout.write(str(num_dic[num_list[i]]) + ' ')
