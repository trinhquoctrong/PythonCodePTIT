# SỐ THUẬN NGHỊCHTRONG MA TRẬN

def tn(n):
    s = str(n)
    if len(s) < 2:
        return False
    return s == s[::-1]

n, m = map(int, input().split())
A = []
val = -1
for i in range(n):
    B = [int(x) for x in input().split()]
    A.append(B)
    for x in B:
        if tn(x) and val < x:
            val = x

res = []
for i in range(n):
    for j in range(m):
        if A[i][j] == val:
            res.append([i, j])
            
if len(res) == 0:
    print('NOT FOUND')
else:
    print(val)
    for i in res:
        print('Vi tri [%d][%d]' % (i[0], i[1]))