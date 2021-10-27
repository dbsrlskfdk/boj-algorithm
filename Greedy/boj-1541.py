formula = input()
num_list = []
calc_list = []
t = 0

for i in range(len(formula)):
    if formula[i] == '+' or formula[i] == '-' or i == len(formula)-1:
        if i != len(formula) - 1:
            calc_list.append(formula[i])
        if t == 0:
            if formula[i] == '+' or formula[i] == '-':
                num_list.append(int(formula[t:i]))    
                t = i
            else:
                num_list.append(int(formula[t:i+1]))    
                t = i
        else:
            if i == len(formula) - 1:
                num_list.append(int(formula[t+1:i+1]))
            else:
                num_list.append(int(formula[t+1:i]))
                t = i
                
sum = num_list[0]
minus_avail = 1

for i in range(1, len(num_list)):
    if calc_list[i-1] == '-':
        if minus_avail == -1:
            sum -= num_list[i]
        elif minus_avail == 1:
            minus_avail = -1
            sum -= num_list[i]
    elif minus_avail == -1:
        sum -= num_list[i]
    else:
        sum += num_list[i]
        
print(sum)                
