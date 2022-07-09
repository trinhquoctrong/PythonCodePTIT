# số thuận nghịch chẵn

a = []

def solve(s):
    if len(s) > 6:
        return
    if s[0] != '0' and int(s) >= 22 and int(s) not in a:
        a.append(int(s))
    solve('0' + s + '0')
    solve('2' + s + '2')
    solve('4' + s + '4')
    solve('6' + s + '6')
    solve('8' + s + '8')
    
solve('00')
solve('22')
solve('44')
solve('66')
solve('88')
a.sort()

for test in range(int(input())):
    n = int(input())
    for i in a:
        if i < n:
            print(i, end = ' ')
        else:
            break
    print()