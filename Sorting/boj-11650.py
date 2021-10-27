N = [list(map(int, input().split(" "))) for i in range(int(input()))]

def merge(left, right):
    v = list()
    i = 0
    j = 0

    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            v.append(left[i])
            i+=1
        else:
            v.append(right[j])
            j += 1
    
    if i == len(left):
        v = v + right[j:len(right)]
    if j == len(right):
        v = v + left[i:len(left)]
    return v
def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    m = len(a_list) // 2
    left = merge_sort(a_list[0:m])
    right = merge_sort(a_list[m:len(a_list)])

    return merge(left, right)

sort_num = merge_sort(N)
sort_num = merge_sort(N[0:])

for i in range(len(N)):
    print(sort_num[i][0], sort_num[i][1])
