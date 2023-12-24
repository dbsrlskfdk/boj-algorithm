sentence = input()

len_S = len(sentence)
mod_sentence = "@"
for i, s in enumerate(sentence):
    mod_sentence += s
    mod_sentence += "@"
sentence = mod_sentence
len_S = len(sentence)

P = [0] * len_S # i번째 문자 중심 가장 긴 팰린드롬 반지름 크기
r = 0 # i-1단계 까지의 모든 팰린드롬의 끝나는 인덱스 중 가장 큰 값
c = 0 # i-1단계 까지 r의 값이 최대가 되게 하는 중심 인덱스

for i in range(len_S):
    if r < i: # i-1단계 까지 팰린드롬이 끝나는 인덱스 중 가장 큰 값이 현재 탐색하려는 인덱스보다 작다면, 현재(i번쨰)문자 중심 가장 긴 팰린드롬 반지름 크기 = 0 -> 현재 문자는 이전에 탐색한  팰린드롬에 포함되지 않는다는 거니까, 현재 문자 중심 팰린드롬 반지름 크기는 0이 된다.
        P[i] = 0
    else: # i-1단계 까지 팰린드롬 끝나는 인덱스 중 가장 큰 값이 현재 탐색 인덱스를 넘어간다면, 이전 팰린드롬에 현재 문자가 속한다는거임
        P[i] = min(P[2*c - i], r-i) # i의 이전 팰린드롬의 중심 인덱스에 대해서 대칭인 곳에서의 가장 긴 팰린드롬 반지름 크기와, 이전의 팰린드롬이 끝나는 인덱스 중 가장 큰 값에서 현재 인덱스를 뺀 위치까지 중 더 작은 값을 현재 인덱스에서의 초기 반지름 크기로 지정한다. => 진짜 어려움 이렇게 하는 이유에 대한 이해는 Ref: https://m.blog.naver.com/jqkt15/222108415284 확인
        
    while (i - P[i] - 1 >= 0 and i + P[i] + 1 < len_S) and (sentence[i - P[i] -1] == sentence[i + P[i] + 1]): # 현재 문자에 대해서 최대 팰린드롬 반지름 탐색
        P[i] += 1
        
    if r < i + P[i]: # i-1단계 까지 팰린드롬이 끝나는 인덱스 중 가장 큰 값이, 현재보다 더 작다면, 업데이트 해줘야함
        r = i + P[i] # 팰린드롬이 끝나는 인덱스 업데이트
        c = i # 더 큰 반지름이 나오는 중심 인덱스 업데이트
        
dp = [float('inf')] * len_S
dp[0] = 0
for t in range(1, len_S):
    if sentence[t] == "@" and P[t] == 0:
        dp[t] = dp[t-1]
        continue
    dp[t] = dp[t] if dp[t] < dp[t-1] + 1 else dp[t-1] + 1
    
    for j in range(1, P[t]+1):
        st = t - j -1
        ed = t + j
        if st < 0:
            dp[ed] = 1
            continue
        dp[ed] = dp[ed] if dp[ed] < dp[st] + 1 else dp[st] + 1

print(dp[len_S-1])