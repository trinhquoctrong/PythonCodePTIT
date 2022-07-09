# XOAY MẢNG

for test in range(int(input())):
    n, d = map(int, input().split())
    A = [int(x) for x in input().split()]
    A = A[d:n] + A[0:d]
    print(*A, sep = ' ')