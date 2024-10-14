N = int(input())
formula = input()

operands = [c for c in formula if c.isdigit()] 
operators = [c for c in formula if not c.isdigit()]
ans = -float("inf")
def dfs(p, prev_sum):
    global ans
    if p >= len(operators):
        ans = max(ans, int(prev_sum))
        return
    
    dfs(p+1, str(eval(prev_sum + operators[p] + operands[p+1])))

    if p + 1 < len(operators):
        dfs(p+2, str(eval(prev_sum+operators[p]+
                          str(eval(operands[p+1]+operators[p+1]+operands[p+2])))))
        
dfs(0, operands[0])

print(ans)