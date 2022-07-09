# MA TRẬN - 1

for test in range(1):
    n = int(input())
    A = []
    for i in range(n):
        A.append([int(x) for x in input().split()])
    k = int(input())
    
    nguong = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                nguong -= A[i][j]
            elif j < i:
                nguong += A[i][j]
    nguong = abs(nguong)
    if nguong <= k:
        print('YES')
    else:
        print('NO')
    print(nguong)

    