import sys

input = sys.stdin.readline

N = int(input())
coords = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    coords.append((x1, y1, x2, y2))
    
def CCW(line_1, line_2):
    x1, y1, x2, y2 = line_1 # A(x1, y1), B(x2, y2)
    x3, y3, x4, y4 = line_2 # C(x3, y3), D(x4, y4)
    
    # (A, B, C), (A, B, D) 와 (C, D, A), (C, D, B)의 외적의 부호가 서로 다르면 교차한다.
    outer_product_1 = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) # A, B, C 외적 : x1y2 + x2y3 + x3y1 - (x2y1 + x3y2 + x1y3)
    outer_product_2 = (x2-x1)*(y4-y1) - (y2-y1)*(x4-x1) # A, B, D 외적 : x1y2 + x2y4 + x4y1 - (x2y1 + x4y2 + x1y4)
    outer_product_3 = (x4-x3)*(y1-y3) - (y4-y3)*(x1-x3) # C, D, A 외적 : x3y4 + x4y1 + x1y3 - (x4y3 + x1y4 + x3y1)
    outer_product_4 = (x4-x3)*(y2-y3) - (y4-y3)*(x2-x3) # C, D, B 외적 : x3y4 + x4y2 + x2y3 - (x4y3 + x2y4 + x3y2)
    
    if outer_product_3 * outer_product_4 <= 0 and outer_product_1 * outer_product_2 <= 0:
        if outer_product_3*outer_product_4 == 0 and outer_product_1*outer_product_2 == 0: # 둘이 일직선이 되는 경우, 상대적인 위치를 비교하여 교차 판단
            max_a_b = (max(x1, x2), max(y1, y2))
            min_a_b = (min(x1, x2), min(y1, y2))
            max_c_d = (max(x3, x4), max(y3, y4))
            min_c_d = (min(x3, x4), min(y3, y4))
            
            if not((max_a_b[0] >= min_c_d[0] and max_a_b[1] >= min_c_d[1]) and (max_c_d[0] >= min_a_b[0] and max_c_d[1] >= min_a_b[1])):
                return False
            
        return True # line_1 , line_2 교차여부
    else:
        return False
    
    
cnt = [1] * N
parents = [i for i in range(N)]

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y: # 트리의 루트 노드가 같다면
        return # 넘어감
    else:
        if x < y: # 루트 노드가 작은쪽으로 몰아줌
            parents[y] = x
            cnt[x] += cnt[y]
        else:
            parents[x] = y
            cnt[y] += cnt[x]
            

for i in range(N):
    for j in range(i+1, N):
        if CCW(coords[i], coords[j]):
            union(i, j)
            
for i in range(N):
    parents[i] = find(parents[i])
            
print(len(set(parents)))
print(max(cnt))