def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0: # left에 들어온 list와 right에 들어온 list가 크기가 존재한다면 시행
        if len(left) > 0 and len(right) > 0: # 둘 다 list의 요소가 존재하면, 
            if left[0] <= right[0]: # left의 값이 right의 값보다 작으면
                result.append(left[0]) # left 의 값을 임시 list에 추가 해준다. -> 오름차순 정렬 시행 
                left = left[1:] # left 리스트는 하나를 정렬 시켰으므로, 1부터 시작하는 것으로 초기화
            else:
                result.append(right[0]) # right의 값이 left 보다 작으면, 임시list에 추가 해주어 오름차순 정렬을 시행한다.
                right = right[1:] # 똑같이 right 리스트의 하나를 정렬 시켰으므로, 하나 뽑고 초기화
        elif len(left) > 0 : # left에만 요소가 존재하면
            result.append(left[0]) # right은 없는거니까, left의 값을 추가 해준다.
            left = left[1:] # 뽑아주고, 1부터 초기화
        elif len(right) > 0: # 똑같이 right에만 요소가 존재하면
            result.append(right[0])  # left는 없는거니까, right의 요소값을 추가
            right = right[1:]
    return result # 합병이 끝난 임시 list를 반환

def merge_sort(a_list):
    if len(a_list) <= 1: # list의 사이즈가 1보다 작거나 같아지면, 분할이 끝난걸로 생각, return
        return a_list

    mid = len(a_list) // 2 # 가운데로 나뉘는 지점
    left_list = a_list[:mid]
    right_list = a_list[mid:] # 가운데를 기준으로 left 와 right로 나뉘어주고
    left_list = merge_sort(left_list) # left 쪽도 재귀적으로 mergesort 시행
    right_list = merge_sort(right_list)
    return merge(left_list, right_list) # 재귀적으로 나눠놓은 list들을 합쳐서 반환
#==========================================
N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))

sort_num = merge_sort(num_list)
#============================================
for i in range(len(sort_num)):
    print(sort_num[i])
