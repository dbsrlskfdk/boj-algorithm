A, B = map(int, input().split(" "))

GCD = 1
LCM = A * B
for i in range(min(A, B), 1, -1):
    if A % i == 0 and B % i == 0:
        GCD = i
        break

for i in range(max(A,B), A*B+1):
    if i % A == 0 and i % B == 0:
        LCM = i
        break

print(GCD)
print(LCM)
