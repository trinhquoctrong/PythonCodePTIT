# bộ ba nguyên tố cùng nhau

def tc(a, b):
    while b > 0:
        c = b
        b = a % b
        a = c
    if a == 1:
        return True
    else:
        return False

l, r = map(int, input().split())
a = []

for i in range(l, r-1):
    for j in range(i+1, r):
        if tc(i, j):
            a.append([i, j])
    
for x in a:
    for i in range(x[1]+1, r+1):
        if tc(x[0], i) and tc(x[1], i):
            print('(' + str(x[0]) + ', ' + str(x[1]) + ', ' + str(i) + ')')
