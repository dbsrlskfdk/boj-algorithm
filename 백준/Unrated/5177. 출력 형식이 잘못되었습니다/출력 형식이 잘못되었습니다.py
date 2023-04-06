import re

K = int(input())
stop_word = r"()[]{}.,;:"
def sub_word(x):
    if x in stop_word:
        x = " " + x + " "
        return x
    else:
        return x.lower()
p = re.compile(r"(?<!\S)\w+(?!\S)")
for i in range(K):
    s1 = "".join(map(sub_word, input()))
    s2 = "".join(map(sub_word, input()))
    s1_union = set(p.findall(s1))
    s2_union = set(p.findall(s2))
    if s1_union == s2_union:
        print(f"Data Set {i+1}: equal")
    else:
        print(f"Data Set {i+1}: not equal")
    print()