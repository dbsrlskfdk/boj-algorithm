N = int(input())
M = int(input())
S = input()

cnt = 0
st = 0
pattern = 0

while st < M - 2:
    if S[st] == "I" and S[st+1] == "O" and S[st+2] == "I":
        pattern += 1
        
        if pattern == N:
            cnt += 1
            pattern -= 1
        
        st += 1 # 어차피 IOI가 나왔으면, 바로 다음 문자는 볼 필요없이 O니까 
    else:
        pattern = 0
    st += 1

print(cnt)