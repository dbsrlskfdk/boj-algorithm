import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split())) # left - mid - right
postorder = list(map(int, input().split())) # left - right - mid
# preorder: mid - left - right 

def dfs(in_order_st, post_order_st, length):
    if not length:
        return
    if length == 1:
        print(inorder[in_order_st], end=" ")
        return
    
    
    left_length = inorder.index(postorder[post_order_st+length-1]) - in_order_st
    
    print(inorder[in_order_st+left_length], end=" ")
    dfs(in_order_st, post_order_st, left_length)
    dfs(in_order_st + left_length+1, post_order_st + left_length, length-left_length-1)
    
dfs(0, 0, n)