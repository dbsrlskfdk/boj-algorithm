from collections import defaultdict

N = int(input())
graphs = defaultdict(dict)

for _ in range(N):
    v, l, r = input().split()
    
    if l != ".":
        graphs[v]["left"] = l
    else:
        graphs[v]["left"] = None
    if r != ".":
        graphs[v]["right"] = r
    else:
        graphs[v]["right"] = None
        
def preorder(v):
    if v == None:
        return
    print(v, end="")
    preorder(graphs[v]["left"])
    preorder(graphs[v]["right"])
    
def inorder(v):
    if v == None:
        return
    inorder(graphs[v]['left'])
    print(v, end="")
    inorder(graphs[v]['right'])
    
def postorder(v):
    if v == None:
        return
    postorder(graphs[v]['left'])
    postorder(graphs[v]['right'])
    print(v, end="")
    
preorder("A")
print("")
inorder("A")
print("")
postorder("A")