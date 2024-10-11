S = input()
T = input()
flag = False
def dfs(a):
    global flag
    if a == S:
        flag = True
        return
    elif len(a) == 0:
        return
    
    if a[-1] == "A":
        dfs(a[:-1])
    if a[0] == "B":
        dfs(a[::-1][:-1])
        
        
dfs(T)

if flag:
    print(1)
else:
    print(0)