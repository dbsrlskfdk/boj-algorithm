N, K = map(int, input().split(" "))
K = min(N-K, K)

cnt_2 = 0
cnt_5 = 0

tmp_1 = N
tmp_2 = N

while tmp_1 // 2 != 0:
    cnt_2 += tmp_1 // 2
    tmp_1 //= 2
while tmp_2 // 5 != 0:
    cnt_5 += tmp_2 // 5
    tmp_2 //= 5


tmp_1 = K
tmp_2 = K
while tmp_1 // 2 != 0:
    cnt_2 -= tmp_1 // 2
    tmp_1 //= 2

while tmp_2 // 5 != 0:
    cnt_5 -= tmp_2 // 5
    tmp_2 //= 5

tmp_1 = N-K
tmp_2 = N-K
while tmp_1 // 2 != 0:
    cnt_2 -= tmp_1 // 2
    tmp_1 //= 2

while tmp_2 // 5 != 0:
    cnt_5 -= tmp_2 // 5
    tmp_2 //= 5

print(min(cnt_2, cnt_5))        
