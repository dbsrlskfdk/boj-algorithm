import sys
input = sys.stdin.readline

N, M, V = map(int, input().split(" "))
C = list(map(int, input().split(" ")))

for _ in range(M):
    K = int(input())
    if K >= N: # K가 노드 갯수보다 길다는건 -> 꼬리가 연결된 곳을 넘어간 것
        K -= N
        if K >= N-V+1:
            K = K % (N-V+1)
        K += V-1
    print(C[K])