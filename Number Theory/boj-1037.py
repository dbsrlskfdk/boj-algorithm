N = int(input())
divisor = list(map(int, input().split(" ")))

if N == 1:
    print(divisor[0] ** 2)
else:
    print(min(divisor) * max(divisor))
