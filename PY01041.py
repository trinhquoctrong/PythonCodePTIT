# số tăng giảm

def solve(n):
    if len(n) < 3:
        return False
    i = 0
    idx = 0
    while i < len(n)-1:
        if n[i] < n[i+1]:
            i += 1
            idx = i     
        else:
            break
    
    for i in range(idx, len(n)-1):
        if n[i] <= n[i+1]:
            return False
    return True

for test in range(int(input())):
    if solve(input()):
        print('YES')
    else:
        print('NO')