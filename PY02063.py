# TÍCH LỚN NHẤT

n = int(input())
A = [int(x) for x in input().split()]
A.sort()
B = []

B.append(A[0] * A[1])               # 2  số đầu
B.append(A[0] * A[1] * A[n-1])      # 2 số đầu, 1 số cuối
B.append(A[n-2] * A[n-1])           # 2 số cuối
B.append(A[n-3] * A[n-2] * A[n-1])  # 3 số cuối

print(max(B))