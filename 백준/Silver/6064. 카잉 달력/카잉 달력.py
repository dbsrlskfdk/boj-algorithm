T = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(T):
    M, N, x, y = map(int, input().split())
    # x < M => x` = x+1 else x` = 1
    # y < N => y` = y+1 else y` = 1
    # M=10, N=12 <M:N> Follows the sequence rule below.
    # 1. <1:1> , 2. <2:2>, 3. <3:3>, 4. <4:4>, 5. <5:5>, ..., 9. <9:9>, nums // M == 0, nums // N == 0
    # 10. <10:10>, 11. <1:11>,  nums // M == 1, nums // N == 0
    # 12. <2:12>, 13. <3:1>, 14. <4:2>, 15. <5:3>, 16. <6:4>, 17. <7:5>, 18. <8:6>, 19. <9:7>, nums // M == 1, nums // N == 1
    # 20. <10:8>, 21. <1:9>, 22. <2:10>, 23. <3:11>, nums // M == 2, nums // N == 1
    # 24. <4:12>, 25. <5:1>, 26. <6:2>, 27. <7:3>, 28. <8:4>, 29. <9:5>, nums // M == 2, nums // N == 2
    # 30. <10:6>, 31. <1:7>, 32. <2:8>, 33. <3:9>, 34. <4:10>, 35. <5:11>, nums // M == 3, nums // N == 2
    gcd_num = gcd(M, N)
    a = set([M * i + x % M for i in range(N // gcd_num)]) # 최소공배수를 전체 다 돌면서 구하는 것보다, 최소공배수를 구할 상대를 최대공약수로 나눈 몫만큼범위에서의 나머지(x)가 나오는 모든 숫지를 구하는 것이 더 빠름.
    b = set([N * i + y % N for i in range(M // gcd_num)])
    inter_set = a.intersection(b)
    if len(inter_set) != 0:
        if inter_set == {0}:
            print(lcm(M, N))
        else:
            print(inter_set.pop())
    else:
        print(-1)