def dp(n):
    tmp = [1, 2]
    for i in range(1, n):
        p2 = tmp[1]

        tmp[1] = (tmp[0] + tmp[1]) % 15746
        tmp[0] = (p2)%15746
    
    return tmp[0]
  
  
N = int(input())
print(dp(N))

#특성방정식의 해결... 오버플로우 뜸 그냥 알아만 두기
# a(n+2) = p * a(n) + q * a(n+1) ==> x^2 = p * x + q 의 방정식의 해를 x = t , s 라고 하면
# a(n) = C1*(t)**n + C2*(s)**n 으로 점화식의 일반항이 나온다. --> a1 과 a2 의 정보를 이용해서, C1과 C2 미정계수 정해주면 끝.

def func(n):
    return ((5-5**0.5) / 10 )*(((1 - 5**0.5) / 2) ** n)  + ((5+5**0.5)/ 10) * (((1 + 5**0.5)/2) ** n)
N = int(input())
print(func(N) % 15746)
