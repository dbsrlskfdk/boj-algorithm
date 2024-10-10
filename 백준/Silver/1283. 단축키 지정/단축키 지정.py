import re

N = int(input())
shortcuts = set()
for _ in range(N):
    words = input()
    mod_words = ""
    for m in re.finditer(r"\w+", words):
        if words[m.start()].lower() not in shortcuts:
            mod_words = words[:m.start()]+"["+words[m.start()]+"]"+words[m.start()+1:]
            shortcuts.add(words[m.start()].lower())
            break
    

    for i, m in enumerate(words):
        if mod_words == "" and (m != " " and m.lower() not in shortcuts):
            mod_words = words[:i] + "[" + words[i] + "]"+words[i+1:]
            shortcuts.add(m.lower())
            break
        

    if not mod_words:
        mod_words = words
    
    print(mod_words)