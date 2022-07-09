# BÀI TOÁN ĐẾM

n = int(input())
A = []
while len(A) < n:
    A = A + [int(x) for x in input().split()]

if max(A) == n:
    print('Excellent!')
else:
    for i in range(1, max(A)):
        if i not in A:
            print(i)