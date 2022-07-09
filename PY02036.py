# LIỆT KÊ CẶP SỐ NGUYÊN TỐ CÙNG NHAU

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
A = [int(x) for x in input().split()]
A.sort()

for i in range(n):
    for j in range(i+1, n):
        if gcd(A[i], A[j]) == 1:
            print(A[i], A[j])