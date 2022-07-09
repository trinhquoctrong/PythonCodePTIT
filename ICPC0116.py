# CON SỐ DUYÊN NỢ

def check(s):
    if s[0] == s[len(s)-1]:
        return 'YES'
    else:
        return 'NO'

for test in range(int(input())):
    print(check(input()))