n, m = map(int, input().split())
known_nums = list(map(int, input().split())) if m != 0 else []

nums = 0
passwords = [0] * n

def password(k):
    global nums
    if k == n:
        for c in known_nums:
            if c not in passwords:
                return
        nums += 1        
        return

    for i in range(10):
        passwords[k] = i
        password(k+1)
        
password(0)
print(nums)