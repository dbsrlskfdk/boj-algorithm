from collections import defaultdict

a = defaultdict(int)
for _ in range(3):
    a[int(input())] += 1
listed_a = list(a.keys())
summation = sum([p[0]*p[1] for p in a.items()])

if summation == 180:
    if len(a) == 1:
        print("Equilateral")
    elif len(a) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")