# KIỂM TRA HỆ CƠ SỐ 3

def solve(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return 'NO'
    return 'YES'

for test in range(int(input())):
    print(solve(input()))