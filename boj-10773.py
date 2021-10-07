import sys
stack_list = []
sum = 0
N = int(input())

for i in range(N):
    command = int(input())
    
    if command != 0:
        sum += command
        stack_list.append(command)
    elif command == 0:
        sum -= stack_list[len(stack_list)-1]
        stack_list = stack_list[:len(stack_list)-1]

print(sum)
