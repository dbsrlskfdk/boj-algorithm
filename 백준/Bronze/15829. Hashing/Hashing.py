L = int(input())
words = input()
summ = 0
char_to_idx = {v: i+1 for i, v in enumerate("abcdefghijklmnopqrstuvwxyz")}

for i in range(L):
    summ += char_to_idx[words[i]] * (31 ** i)
    
print(summ % 1_234_567_891)