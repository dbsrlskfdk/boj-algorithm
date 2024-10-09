import math

H, W, N, M = map(int, input().split()) # W 열, H 행, 세로 N칸 가로 M칸 이상 비우고앉아야함
horizon_n = int((W + 2*M - (2*M+1)) / (M+1) + 1)
vertical_n = int((H + 2*N - (2*N+1)) / (N+1) + 1)
print(horizon_n*vertical_n)