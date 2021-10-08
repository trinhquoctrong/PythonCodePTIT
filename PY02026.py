# tập hợp số bằng nhau

n = input()
A = list(set(int(i) for i in input().split()))
B = list(set(int(i) for i in input().split()))
A.sort()
B.sort()
if A == B:
    print('YES')
else:
    print('NO')