from copy import deepcopy

def solution(n, k, cmd):
    answer = ''
    cur = k
    deleted = [False for _ in range(n)]
    deleted_list = []
    linked_list = {}
    
    for i in range(n):
        if i-1 >= 0:
            if i+1 < n:
                linked_list[i] = {"prev": i-1, "next": i+1}
            else:
                linked_list[i] = {"prev": i-1, "next": None}
        else:
            linked_list[i] = {"prev": None, "next": i+1}
            
    for c in cmd:
        command = c.split(" ")

        if command[0] == "D":
            param = int(command[1])
            while param > 0:
                cur = linked_list[cur]["next"]
                param -= 1
            # print(f"Selected: {characters[cur]}")
        elif command[0] == "U":
            param = int(command[1])
            while param > 0:
                cur = linked_list[cur]["prev"]
                param -= 1
            # print(f"Selected: {characters[cur]}")
        elif command[0] == "C":
            deleted_list.append(cur)
            deleted[cur] = True
            # print(f"Deleted: {characters[cur]}")
            if linked_list[cur]["next"] is not None:
                linked_list[linked_list[cur]["next"]]["prev"] = linked_list[cur]["prev"]
            if linked_list[cur]["prev"] is not None:
                linked_list[linked_list[cur]["prev"]]["next"] = linked_list[cur]["next"]
            cur = linked_list[cur]["next"] if linked_list[cur]["next"] is not None else linked_list[cur]["prev"]
            # print(f"Deleted After Selected: {characters[cur]}")
        elif command[0] == "Z": 
            undo = deleted_list.pop()
            deleted[undo] = False
            # print(f"Undo: {characters[undo]}")
            if linked_list[undo]["next"] is not None:
                linked_list[linked_list[undo]["next"]]["prev"] = undo
            if linked_list[undo]["prev"] is not None:
                linked_list[linked_list[undo]["prev"]]["next"] = undo
            # print(f"Undo After Selected: {characters[cur]}")
        # print(f"cur: {cur}")
    
    for delete in deleted:
        if not delete:
            answer+="O" 
        else:
            answer+="X"
    return answer