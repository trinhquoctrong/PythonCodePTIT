# SỐ ĐẸP TRONG MA TRẬN

n, m = map(int, input().split())
C = []
A = []
for i in range(n):
    B = [int(x) for x in input().split()]
    A.append(B)
    C.append(max(B))
    C.append(min(B))
    
val = max(C) - min(C)
C.clear()
for i in range(n):
    for j in range(m):
        if A[i][j] == val:
            C.append([i, j])

if len(C) == 0:
    print('NOT FOUND')
else:
    print(val)
    for i in C:
        print('Vi tri [%d][%d]' % (i[0], i[1]))