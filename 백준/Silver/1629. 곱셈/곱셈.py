A, B, C = map(int, input().split())
mod_sum = 1

while B:
    if B & 1: # 홀수면
        mod_sum *= A
        mod_sum = mod_sum % C
    
    A *= A
    A = A % C
    B = B >> 1 # B = B // 2
    
print(mod_sum)