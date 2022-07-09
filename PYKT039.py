# DÃY SỐ PHÙ HỢP

def check(A, B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return 'NO'
    return 'YES'

for test in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()
    print(check(A, B))
        