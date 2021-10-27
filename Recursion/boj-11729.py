N = int(input())
cnt = 0
movement = []
def move(start, to):
    global cnt
    cnt += 1
def hanoi(N, li=movement, start=1, to=3, via=2 ):
    if N == 1:
        move(start, to)
        li.append([start, to])
    else:
        hanoi(N-1, li, start, via, to)
        move(start, to)
        li.append([start, to])
        hanoi(N-1, li, via, to, start)
        
hanoi(N)
print(cnt)
for i in range(len(movement)):
    print(movement[i][0], movement[i][1])
