import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

bin_tree_pre = []

while True:
    try:
        input_num = int(input())
        bin_tree_pre.append(input_num)
    except:
        break
        
def dfs(root_node, order_res):
    l_node = []
    r_node = []
    for i in range(1, len(order_res)):
        if order_res[i] < root_node:
            l_node.append(order_res[i])
        else:
            r_node.append(order_res[i])
    if l_node:
        dfs(l_node[0], l_node)
    if r_node:
        dfs(r_node[0], r_node)
    print(root_node)
    
dfs(bin_tree_pre[0], bin_tree_pre)