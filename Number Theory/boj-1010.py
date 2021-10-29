T = int(input())
bridge_list = [list(map(int,input().split(" "))) for _ in range(T)]

for t in range(T):
    bin = [[0 for _ in range(bridge_list[t][1]+1)] for _ in range(bridge_list[t][1]+1)]
    bin[0][0] = 1
    bin[1][0] = 1
    bin[1][1] = 1

    for i in range(2, bridge_list[t][1]+1):
        for j in range(0, i+1):
            if j == 0 or j == i:
                bin[i][j] = 1
            else:
                bin[i][j] = (bin[i-1][j-1] + bin[i-1][j])
            
            
    print(bin[bridge_list[t][1]][bridge_list[t][0]])  
