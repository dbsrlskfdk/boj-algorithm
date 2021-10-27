import sys
stack_list = []
N = int(input())

for i in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        stack_list.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])
            stack_list = stack_list[:len(stack_list)-1]
    elif command[0] == 'size':
        print(len(stack_list))
    elif command[0] == 'empty':
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])
