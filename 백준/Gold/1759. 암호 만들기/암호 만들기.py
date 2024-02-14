L, C = map(int, input().split())
alphabets = input().split()
alphabets.sort()

def dfs(cur, vowel, conso, l, chars, visited):
    if vowel + conso == l:
        if vowel >= 1 and conso >= 2:
            print(chars)
        return
    
    for i in range(cur, C):
        if not visited[i]:
            visited[i] = True
            if alphabets[i] in "aeiou":
                dfs(i, vowel+1, conso, l, chars+alphabets[i], visited)
            else:
                dfs(i, vowel, conso+1, l, chars+alphabets[i], visited)
            visited[i] = False
    
dfs(0, 0, 0, L, "", [False]*C)   