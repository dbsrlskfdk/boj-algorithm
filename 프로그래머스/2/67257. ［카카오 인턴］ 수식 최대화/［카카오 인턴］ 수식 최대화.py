import re

def calc(operand, operation_list, operation_level):
    for op in operation_level:
        stack_operand = []
        stack_operation = []
        stack_operand.append(operand[0])
        for i in range(len(operation_list)):
            stack_operand.append(operand[i+1])
            stack_operation.append(operation_list[i])
            
            if stack_operation[-1] == op:
                b = stack_operand.pop()
                a = stack_operand.pop()
                operation = stack_operation.pop()
                
                stack_operand.append(str(eval(a+operation+b)))
        operand = stack_operand
        operation_list = stack_operation
    return abs(int(stack_operand[-1]))

max_res = 0

def dfs(i, ope, visited, operand, operation_list, operation_sort):
    global max_res
    if i == len(operation_sort):
        operation_level = {c: t for t, c in enumerate(ope)}
        max_res = max(max_res, calc(operand, operation_list, operation_level))
        return
    
    for j in range(len(operation_sort)):
        if not visited[j]:
            visited[j] = True
            dfs(i+1, ope+[operation_sort[j]], visited, operand, operation_list, operation_sort)
            visited[j] = False
            
def solution(expression):
    operand = re.findall(r"([\d]+)", expression)
    operation_list = re.findall(r"([^\d]+)", expression)
    operation_sort = list(set(operation_list))
    
    visited = [False] * len(operation_sort)
    
    dfs(0, [], visited, operand, operation_list, operation_sort)
    return max_res