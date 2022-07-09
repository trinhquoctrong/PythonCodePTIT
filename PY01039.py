# kiểm tra só đẹp

def solve(s):
    for i in range (0, len(s), 2):
        if s[i] != s[0]:
            return False
    for i in range (1, len(s), 2):
        if s[i] != s[1]:
            return False
    return True


for test in range(int(input())):
    if solve(input()):
        print('YES')
    else:
        print('NO')