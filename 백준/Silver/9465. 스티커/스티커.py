T = int(input())
for _ in range(T):
	n = int(input())
	sticker = [list(map(int, input().split(" "))) for _ in range(2)]
	score = [[0] * (n+1) for _ in range(2)]

	score[0][0] = 0
	score[1][0] = 0
	score[0][1] = sticker[0][0]
	score[1][1] = sticker[1][0]

	for i in range(2, n+1):
		score[0][i] = max(score[1][i-1], score[1][i-2]) + sticker[0][i-1]
		score[1][i] = max(score[0][i-1], score[0][i-2]) + sticker[1][i-1]

	print(max(score[0][n], score[1][n]))