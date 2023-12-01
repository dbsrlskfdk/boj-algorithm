N = int(input())
M = int(input())
S = input()

search_word = "IO" * N + "I"
cnt = 0

for i in range(M - (2*N+1) + 1):
    if search_word == S[i:i+2*N+1]:
        cnt += 1
    
print(cnt)