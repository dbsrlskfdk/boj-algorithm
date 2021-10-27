from collections import Counter

def most_frequency(sort_num):
    a = Counter(sort_num)
    a = a.most_common()

    max_val = a[0][1]
    tmp = []

    for i in range(len(a)):
        if a[i][1] == max_val:
            tmp.append(a[i])
        else:
            break;
    
    if len(tmp) == 1:
        return tmp[0][0]
    else:
        return tmp[1][0]
    
            

N = int(input())
num_list = []
num_dic = {}
for i in range(N):
    tmp = int(input())
    num_list.append(tmp)


sort_num = sorted(num_list)

avg = round(sum(num_list) / N)
mid = sort_num[len(sort_num) // 2]
most_fre = most_frequency(sort_num)
range_val = max(num_list) - min(num_list)

print("%d" %avg)
print("%d" %mid)
print("%d " %most_fre)
print("%d" %range_val)
