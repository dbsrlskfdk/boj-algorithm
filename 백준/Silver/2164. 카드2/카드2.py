from collections import deque

N = int(input())

que = deque()
for i in range(1, N+1):
    que.appendleft(i)
    
while len(que) != 1:
    que.pop()
    tmp = que.pop()
    que.appendleft(tmp)
    
print(que.pop())