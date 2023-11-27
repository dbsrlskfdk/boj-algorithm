import sys

input = sys.stdin.readline

M = int(input())

S = set()
alter_set = set([str(i) for i in range(1, 20+1)])
for _ in range(M):
    cmd = input().strip().split(" ")
    
    if cmd[0] == "add":
        S.add(cmd[1])
    elif cmd[0] == "all":
        S.clear()
        S.update(alter_set)
    elif cmd[0] == "empty":
        S.clear()
    elif cmd[0] == "remove":
        S.discard(cmd[1])
    elif cmd[0] == "check":
        print(1) if cmd[1] in S else print(0)
    elif cmd[0] == "toggle":
        S.remove(cmd[1]) if cmd[1] in S else S.add(cmd[1])
    