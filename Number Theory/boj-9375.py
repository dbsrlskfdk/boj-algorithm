T = int(input())
dresses = []

for i in range(T):
  dress = {}
  n = int(input())
  for j in range(n):
    name, sort = input().split(" ")
    if sort not in dress:
      dress[sort] = 1
     else:
      dress[sort] += 1
  dresses.append(dress)
  
def calc_dress(dress):
  sum = 1
  if len(dress) == 1:
    return list(dress.values())[0]
  else:
    for _, num in dress.items():
      sum *= (num+1)
      
  sum -= 1
  return sum

for i in range(T):
  print(calc_dress(dresses[i]))
