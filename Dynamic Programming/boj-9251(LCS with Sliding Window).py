import copy

C = input()
R = input()

LENGTH = [[0, 0], [0, 0]]
LENGTH_width = []

def LCS_Length(C, R):
    for i in range(1, len(R)+1):
        for j in range(1, len(C)+1):
            if  R[i-1] == C[j-1]:
                if i != 1:
                    LENGTH[0] = copy.deepcopy(LENGTH_width[0])
                    del LENGTH_width[0]
                LENGTH[1][1] = LENGTH[0][0] + 1
                
                if i == len(R) and j == len(C):
                    return LENGTH[1][1]

                LENGTH_width.append(copy.deepcopy(LENGTH[1]))
                # print(f'LENGTH : {LENGTH}')     
                # print(f'LENGTH_width : {LENGTH_width}')
                for t in range(2):
                    tmp = LENGTH[t][1]
                    LENGTH[t][0] = tmp
                    LENGTH[t][1] = 0
            else:
                if i != 1:
                    LENGTH[0] = copy.deepcopy(LENGTH_width[0])
                    del LENGTH_width[0]
                LENGTH[1][1] = max(LENGTH[1][0], LENGTH[0][1])
                
                if i == len(R) and j == len(C):
                    return LENGTH[1][1]
                LENGTH_width.append(copy.deepcopy(LENGTH[1]))
                # print(f'LENGTH : {LENGTH}')     
                # print(f'LENGTH_width : {LENGTH_width}')
                for t in range(2):
                    tmp = LENGTH[t][1]
                    LENGTH[t][0] = tmp
                    LENGTH[t][1] = 0
        
            
        # print("==========================")
        if i != len(R):
            LENGTH[1] = copy.deepcopy([0, 0])

print(LCS_Length(C, R))            
