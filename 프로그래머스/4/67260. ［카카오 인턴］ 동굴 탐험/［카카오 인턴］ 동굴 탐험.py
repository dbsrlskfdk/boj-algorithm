from collections import defaultdict, deque

def solution(n, path, order):
    answer = True
    graphs = defaultdict(list)
    for st, ed in path:
        graphs[st].append(ed)
        graphs[ed].append(st)
    que = deque([0])
    visited = defaultdict(bool)
    order_graph = defaultdict(list)
    
    while que:
        v = que.popleft()
        visited[v] = True

        for i in graphs[v]:
            if not visited[i]:
                que.append(i)
                order_graph[i].append(v)
    for i, v in order:
        order_graph[v].append(i)
    
    # Cycle 체크   
    return not is_cyclic_check(order_graph, n)

def is_cyclic_check(order_graph, n):
    visited = defaultdict(bool)
    on_stack = defaultdict(bool)
    
    stack = deque([])
    
    for v in range(n):
        if visited[v]:
            continue
            
        stack.append(v)
        
        while stack:
            top = stack[-1] # Stack의 Top을 확인
            if not visited[top]: # 만약 Top을 방문하지 않았다면,
                visited[top] = True # 방문 표시
                on_stack[top] = True # 스택 위에 있음을 표시
            else:
                on_stack[top] = False # 만약 Top을 방문했었다면, Stack위에 없음을 표시해주고
                stack.pop() # pop 해준다
            
            for nv in order_graph[top]: # top에 연결된 노드 확인
                if not visited[nv]: # 만약 방문하지 않은 노드라면
                    stack.append(nv) # 스택에 추가.
                elif on_stack[nv]: # 만약 해당 노드가 방문 했으면서, And 스택 위에까지 있다면, 사이클이 생긴 것..
                    return True
            
    
    return False