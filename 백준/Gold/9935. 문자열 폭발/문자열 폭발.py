S = input()
bomb = [c for c in input()]
len_bomb = len(bomb)

stack = []
for i in S:
    stack.append(i)
    if stack[-len_bomb:] ==  bomb:
        for _ in range(len_bomb):
            stack.pop()
            
print(''.join(stack) if stack else "FRULA")