MAX_NUM = 10000

num_list = [int(input()) for i in range(int(input()))]
sorted_list = []

count = [0] * (MAX_NUM + 1)
count_sum = [0] * (MAX_NUM + 1)

for i in range(len(num_list)):
    count[num_list[i]] += 1

count_sum[0] = count[0]
for i in range(1, MAX_NUM+1):
    count_sum[i] = count_sum[i-1] + count[i] # 누적합 구하기, 이전 count_sum과 그다음 숫자의 count를 더해서 누적합 갱신 

sorted_list = [0] * (len(num_list) + 1)

for i in range(len(num_list)-1, -1, -1): # 맨 뒤 위치부터 반복
    sorted_list[ count_sum[ num_list[i] ] ] = num_list[i] # num_list 입력받은 배열의 숫자의 누적합에 해당하는 정렬된 리스트(sorted_list)index에 넣어준다.
    count_sum[num_list[i]] -= 1 # 그리고 해당 숫자의 누적합을 1 감소시켜줌으로써, 다음 그 숫자가 들어가야할 index는 하나 감소된 곳에 저장 되는 것

for i in range(1, len(num_list) + 1):
    print(sorted_list[i])
