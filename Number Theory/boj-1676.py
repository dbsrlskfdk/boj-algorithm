N = int(input())
sum = 0

for i in range(1, N+1):
  tmp = i
  while tmp % 5 == 0:
    sum += 1
    tmp /= 5
    
print(sum)
