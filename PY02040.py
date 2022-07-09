# MA TRẬN - 2

n = int(input())
A = []
for i in range(n):
    A.append([int(x) for x in input().split()])
k = int(input())
    
nguong = 0
for i in range(n):
    for j in range(n):
        if i + j < n-1:
           nguong += A[i][j]
        elif i + j > n-1:
            nguong -= A[i][j]
nguong = abs(nguong)
if nguong <= k:
    print('YES')
else:
    print('NO')
print(nguong)